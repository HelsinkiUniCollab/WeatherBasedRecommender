# cPouta production environment

Production environment is updated automatically every time new code is pushed to main.
Read more here: 

## cPouta cloud service

cPouta is an Infrastructure as a Service (IaaS) cloud provided by [CSC](https://www.csc.fi/)
The cPouta virtual machines can be connected to external IP addresses, and they can be directly accessed on the internet. 

We use cPouta as a production environment for Weather Based Recommender App. Floating IP allocated to our project is 128.214.253.51.

In order to access cPouta cloud, you need to accept terms in [My CSC portal](https://my.csc.fi/projects/2004807). Make sure you are in Project 2004807 -page. Then scroll down and click cPouta in the right column. Accept the terms.


* [What is Pouta](https://docs.csc.fi/cloud/pouta/pouta-what-is/)
* [Security Guidelines in Pouta](https://docs.csc.fi/cloud/pouta/pouta-what-is/)
* [Creating a Virtual Machine in Pouta](https://docs.csc.fi/cloud/pouta/launch-vm-from-web-gui/)

## How to access cPouta instance

1. You need to have an access key (pouta.key) in your .shh folder (/home/{user}/.ssh). If you are missing the key, ask from a team member. 

2. Make sure that you are in .ssh -folder and open the connection from your terminal with command:

`ssh -i .ssh/pouta.key ubuntu@128.214.253.51`


## Basic Docker commands to be used in Pouta

You can check what docker containers are running in which ports with command:

`sudo docker ps`

If application has stopped running you  start it manually with:

`sudo docker compose up -d`

