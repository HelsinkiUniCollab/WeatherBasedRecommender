# cPouta Production Environment

Production environment is updated automatically everytime new code is pushed to the main branch.
Read more about the CI-CD [here](/docs/ci-cd.md).

## cPouta Cloud Service

cPouta is an Infrastructure as a Service (IaaS) cloud provided by [CSC](https://www.csc.fi/).

The cPouta virtual machines can be connected to external IP addresses, which then can be directly accessed on the internet. Floating IP currently allocated to our project is `128.214.253.51`.

In order to access cPouta cloud, you need to accept terms in [My CSC Portal](https://my.csc.fi/projects/2004807). Make sure you are in the project 2004807 page. Then scroll down and click cPouta heading in the right column. Accept the terms.

You can then access the [cPouta Dashboard](https://pouta.csc.fi/dashboard/project/instances/).

## How to access cPouta instance with SSH

1. You need to have an access key named `pouta.key` in your `.ssh` folder. If you are missing the key, ask from a team member. 

2. Make sure that you are in the `.ssh` -folder and open the connection from your terminal with command:

```bash
ssh -i pouta.key ubuntu@128.214.253.51
```

## How to update Ubuntu in Pouta instance

Currently security and other updates to Ubuntu need to be run manually. Open the terminal application and open the SSH access.

```bash
# Fetch updates for the packages
$ sudo apt-get update

# Update the packages
$ sudo apt-get upgrade

# Reboot the Ubuntu box
$ sudo reboot
```

## Basic Docker commands to be used in Pouta

When you have a SSH connection open to Pouta, you can check which docker containers are running and which ports are allocated to them:

```bash
sudo docker ps
```

If the app has stopped running, you can start it manually. These containers should be always running: 
*nginx:latest*, *redis:latest*, *helsinkiunicollab/wbased-back:latest*, *helsinkiunicollab/wbased-front:latest* and *watchtower:latest*.  

If the site is not responding, try restarting the containers using these two commands:

```bash
# Shut down all of the containers
$ sudo docker compose down

# Start all of the containers
$ sudo docker compose up -d
```
Here is a couple of more commands that can be useful in troubleshooting:

```bash
# Get a list of all of the containers
$ sudo docker container ls -a

# Remove unused containers
$ sudo docker container prune

# Remove all of the containers and images
$ sudo docker rm -f $(docker ps -a -q)
$ sudo docker rmi -f $(docker images -a -q)

# create ubuntu_default network it it's removed
$ sudo docker create network ubuntu_default
```

## Removing old Docker images in Pouta

Everytime an update is made, a new image with a tag "latest" is created. This does not remove the old images, which keep piling up. Therefore, we have a cron job running docker prune every night at 3 a.m. UTC. 

```bash
0 3 * * * /snap/bin/docker system prune -a -f
```
You can edit the cron job with command in the root directory of our instance.

```bash
crontab -e
```
## Docker Containers

Currently we have 5 Docker containers up and running, these are:

**wbased-back**: This is the backend service built using the Docker image `ruusukivi/wbased-back:latest`. It has the `watchtower` label to enable automatic updates. The service is set to restart unless manually stopped and it's connected to the network `ubuntu_default`.

**wbased-front**: This is the frontend service built using the Docker image `ruusukivi/wbased-front:latest`. It also has the `watchtower` label for automatic updates. This service is exposed on port `3000` and it's set to restart unless manually stopped. It's also connected to the network `ubuntu_default`.

**nginx**: This is the reverse proxy server. It uses the `nginx` image and it's configured with a custom nginx configuration file. This service is exposed on port `80` and is also connected to the network `ubuntu_default`. It's set to restart unless manually stopped. The nginx reverse proxy is set to route all requests coming to `/api/` to the backend service. This means all client requests must go through the reverse proxy, which provides an additional layer of security.

**redis**: This is a service used for caching.

**watchtower**: This service is used to automatically update the Docker containers. It uses the `containrrr/watchtower` image and it has access to the Docker socket, allowing it to monitor the other services. The command `--label-enable --interval 60` tells Watchtower to only update containers with the specific Watchtower label and to check for updates every 60 seconds.

## Current Pouta Docker configurations

### docker-compose.yml
```bash
version: '3.3'
services:
  wbased-back:
    build: .
    image: ruusukivi/wbased-back:latest
    labels:
      - "com.centurylinklabs.watchtower.enable=true"
    restart: unless-stopped
    networks:
      - ubuntu_default

  wbased-front:
    build: .
    image: ruusukivi/wbased-front:latest
    labels:
      - "com.centurylinklabs.watchtower.enable=true"
    ports:
      - 3000:3000
    restart: unless-stopped
    networks:
      - ubuntu_default

  nginx:
    image: nginx:latest
    depends_on:
      - wbased-back
      - wbased-front
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf
    ports:
      - 80:80
    restart: unless-stopped
    networks:
      - ubuntu_default

  watchtower:
    image: containrrr/watchtower
    environment:
      - WATCHTOWER_PULL_IMAGES=true
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
    restart: unless-stopped
    command: --label-enable --interval 300
    networks:
      - ubuntu_default

  redis:
    image: redis:latest

networks:
  ubuntu_default:
    external: true
```

### nginx.conf
```bash
events {}

http {
  server {
    listen 80;

    location /api {
      proxy_pass http://wbased-back:5000;
      proxy_set_header Host $host;
      proxy_set_header X-Real-IP $remote_addr;
      proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
      proxy_read_timeout 120s;
    }

    location / {
      proxy_pass http://wbased-front:3000/;
    }
  }
}
```
### More information about cPouta

* [What is Pouta](https://docs.csc.fi/cloud/pouta/pouta-what-is/)
* [Security Guidelines in Pouta](https://docs.csc.fi/cloud/pouta/pouta-what-is/)
* [Creating a Virtual Machine in Pouta](https://docs.csc.fi/cloud/pouta/launch-vm-from-web-gui/)

