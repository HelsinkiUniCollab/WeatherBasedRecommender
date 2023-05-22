# CI-CD Pipeline

## CI

The CI pipeline, defined in [ci.yml](../.github/workflows/ci.yml) is run automatically, when a pull request is opened or code is pushed to the main branch.

The CI process ensures the successful execution of frontend and backend tests. Currently, testing is performed locally as the project does not have a staging environment.

The project does not have a staging environment at this point. Testing is done locally.

## CD

Production deployment is done by [cd.yml](../.github//workflows/cd.yml), which deploys to production each time a commit is pushed to the main branch.

## What happens in deployment

* Updated Docker images are pushed to Docker Hub into these repositories:
  * https://hub.docker.com/repository/docker/ruusukivi/wbased-back/general
  * https://hub.docker.com/repository/docker/ruusukivi/wbased-front/general

* [Watchtower](https://containrrr.dev/watchtower/) updates the new images automatically to the instance running in Pouta. No need to do anything manually unless the app is not running in Pouta. 
  * If the app is not running, log in to the Pouta with SSH and run command `sudo docker compose up -d` (more detailed here [Pouta](/docs/pouta.md))
