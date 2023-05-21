# CI-CD Pipeline

## CI

When a pull request is opened or code is pushed to the main, [ci.yml](../.github/workflows/ci.yml) is run automatically.

CI makes sure both frontend and backend tests pass.

## CD

Production deployment is done by [cd.yml](../.github//workflows/ci.yml) which is run everytime something is pushed to main.

What happens in deployment:

* Updated Docker images are pushed to Docker Hub to these repositories:
* * https://hub.docker.com/repository/docker/ruusukivi/wbased-back/general
* * https://hub.docker.com/repository/docker/ruusukivi/wbased-front/general

* [Watchtower](https://containrrr.dev/watchtower/) updates the new images automatically to the instance running in Pouta. No need to do anything manually unless the app is not running in Pouta. App can be started by log in to Pouta with SSH and then running `sudo docker compose up -d`
