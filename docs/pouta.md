# cPouta production environment

Production environment is updated automatically everytime new code is pushed to the main branch.
Read more here: [CI/CD Pipeline](/docs/ci-cd.md)

## cPouta cloud service

cPouta is an Infrastructure as a Service (IaaS) cloud provided by [CSC](https://www.csc.fi/).

The cPouta virtual machines can be connected to external IP addresses, which then can be directly accessed on the internet. Floating IP allocated to our project is 128.214.253.51.

In order to access cPouta cloud, you need to accept terms in [My CSC portal](https://my.csc.fi/projects/2004807). Make sure you are in project 2004807 page. Then scroll down and click cPouta heading in the right column. Accept the terms.

You can then access [cPouta Dashboard](https://pouta.csc.fi/dashboard/project/instances/).

## How to access cPouta instance with SSH

1. You need to have an access key (pouta.key) in your .shh folder. If you are missing the key, ask from a team member. 

2. Make sure that you are in .ssh -folder  (/home/{user}/.ssh) and open the connection from your terminal with command:

`ssh -i .ssh/pouta.key ubuntu@128.214.253.51`

## Basic Docker commands to be used in Pouta

When you have a SSH connection open to Pouta, you can check which docker containers are running and which ports are allocated to them:

`sudo docker ps`

If the app has stopped running, you can start it manually. These containers should be always running: 
*ubuntu-wbased-back-1*, u*buntu-wbased-front-1* and *ubuntu-watchtower-1*.  
To start all these containers manually run command:

`sudo docker compose up -d`

### More information about cPouta

* [What is Pouta](https://docs.csc.fi/cloud/pouta/pouta-what-is/)
* [Security Guidelines in Pouta](https://docs.csc.fi/cloud/pouta/pouta-what-is/)
* [Creating a Virtual Machine in Pouta](https://docs.csc.fi/cloud/pouta/launch-vm-from-web-gui/)

