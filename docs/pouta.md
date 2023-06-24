# cPouta Production Environment

Production environment is updated automatically everytime new code is pushed to the main branch.
Read more here: [CI/CD Pipeline](/docs/ci-cd.md)

## cPouta Cloud Service

cPouta is an Infrastructure as a Service (IaaS) cloud provided by [CSC](https://www.csc.fi/).

The cPouta virtual machines can be connected to external IP addresses, which then can be directly accessed on the internet. Floating IP allocated to our project is 128.214.253.51.

In order to access cPouta cloud, you need to accept terms in [My CSC portal](https://my.csc.fi/projects/2004807). Make sure you are in project 2004807 page. Then scroll down and click cPouta heading in the right column. Accept the terms.

You can then access [cPouta Dashboard](https://pouta.csc.fi/dashboard/project/instances/).

## How to access cPouta instance with SSH

1. You need to have an access key (pouta.key) in your .shh folder. If you are missing the key, ask from a team member. 

2. Make sure that you are in .ssh -folder  `(/home/{user}/.ssh)` and open the connection from your terminal with command:

`ssh -i .ssh/pouta.key ubuntu@128.214.253.51`


## How to update Ubuntu in Pouta instance

Currently security and other updates to Ubuntu need to be run manually. 

1. Open the terminal application and open SSH access.
2. Fetch update software list by running the `sudo apt-get update` command
3. Update Ubuntu software by running the `sudo apt-get upgrade` command
4. Finally, reboot the Ubuntu box by running the `sudo reboot` command.


## Basic Docker commands to be used in Pouta

When you have a SSH connection open to Pouta, you can check which docker containers are running and which ports are allocated to them:

`sudo docker ps`

If the app has stopped running, you can start it manually. These containers should be always running: 
*ubuntu-nginx-1*, *ubuntu-wbased-back-1*, *ubuntu-wbased-front-1* and *ubuntu-watchtower-1*.  

If the site is not responding, first make sure that all containers are shut down and the start all the containers by running these two commands:

`sudo docker compose down`

`sudo docker compose up -d`

To get a list of all containers, run:

`sudo docker container ls -a`

You can remove unused containers with:

`sudo docker container prune`

## Removing old images in Pouta

Everytime an update is made, a new image with tag "latest" is created. This does not remove the old images, which keep piling up. Therefore, we have a cron job running remove-old-images.sh every night at 3 a.m. UTC. 

### remove-old-images.sh
```#!/bin/bash
docker system prune -f
```
You can edit the cron job with command in the root directory of our instance.
```crontab -e
```

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
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
    restart: unless-stopped
    command: --label-enable --interval 60
    networks:
      - ubuntu_default

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

      # Add CORS headers
      if ($request_method = 'OPTIONS') {
        add_header 'Access-Control-Max-Age' 1728000 always;
        add_header 'Content-Type' 'text/plain charset=UTF-8' always;
        add_header 'Content-Length' 0 always;
        return 204;
      }

      add_header 'Access-Control-Allow-Methods' 'GET, POST, OPTIONS' always;
      add_header 'Access-Control-Allow-Headers' 'Authorization, Content-Type' always;
    }

    location / {
      proxy_pass http://wbased-front:3000/;
    }
  }
}

```
**wbased-back**: This is the backend service built using the Docker image `ruusukivi/wbased-back:latest`. It has the `watchtower` label to enable automatic updates. The service is set to restart unless manually stopped and it's connected to the network `ubuntu_default`.

**wbased-front**: This is the frontend service built using the Docker image `ruusukivi/wbased-front:latest`. It also has the `watchtower` label for automatic updates. This service is exposed on port `3000` and it's set to restart unless manually stopped. It's also connected to the network `ubuntu_default`.

**nginx**: This is the reverse proxy server. It uses the `nginx` image and it's configured with a custom nginx configuration file. This service is exposed on port `80` and is also connected to the network `ubuntu_default`. It's set to restart unless manually stopped. The nginx reverse proxy is set to route all requests coming to `/api/` to the backend service. This means all client requests must go through the reverse proxy, which provides an additional layer of security.

**watchtower**: This service is used to automatically update the Docker containers. It uses the `containrrr/watchtower` image and it has access to the Docker socket, allowing it to monitor the other services. The command `--label-enable --interval 60` tells Watchtower to only update containers with the specific Watchtower label and to check for updates every 60 seconds.


### More information about cPouta

* [What is Pouta](https://docs.csc.fi/cloud/pouta/pouta-what-is/)
* [Security Guidelines in Pouta](https://docs.csc.fi/cloud/pouta/pouta-what-is/)
* [Creating a Virtual Machine in Pouta](https://docs.csc.fi/cloud/pouta/launch-vm-from-web-gui/)

