
![image](https://github.com/HelsinkiUniCollab/WeatherBasedRecommender/assets/101641412/319fd929-2ab4-4e13-964b-ae23c8d2e32f)


[![CI](https://github.com/HelsinkiUniCollab/WeatherbasedRecommender/actions/workflows/ci.yml/badge.svg)](https://github.com/HelsinkiUniCollab/WeatherbasedRecommender/actions/workflows/ci.yml)
[![CD](https://github.com/HelsinkiUniCollab/WeatherbasedRecommender/actions/workflows/cd.yml/badge.svg?branch=main)](https://github.com/HelsinkiUniCollab/WeatherbasedRecommender/actions/workflows/cd.yml)
[![Codecov](https://codecov.io/github/HelsinkiUniCollab/WeatherBasedRecommender/branch/main/graph/badge.svg?token=RU4KTLCO85)](https://codecov.io/github/HelsinkiUniCollab/WeatherBasedRecommender)

The purpose of this project is to develop an application that provides users with personalized recommendations for points of interest and routes in Helsinki. It takes into consideration the current weather conditions to enhance the generated suggestions. This application is being created as part of the software [engineering course](https://github.com/HY-TKTL/TKT20007-Ohjelmistotuotantoprojekti/) at the [University of Helsinki](https://www.helsinki.fi/fi).

Application can be accessed here: [Weather-Based Recommender](http://128.214.253.51:3000/)

[License](/LICENSE)

## Instructions

```bash
# Give permissions for a script to specify the backend URL
$ chmod +x generate_local_env.sh

# Run the script and generate a local backend URL
$ ./generate_local_env.sh

# Start the frontend and backend services on ports 5000 and 3000, respectively
$ docker compose up
```

To run the frontend and backend services individually, refer to the instructions provided in the [frontend](/recommender-front/README.md) and [backend](/recommender-back/README.md) README's respectively.

## Documentation

* [Working hours](/docs/hours.md)
* [Team roles](/docs/roles.md)
* [Definition of Done](/docs/dod.md)
* [Git Workflow](/docs/git-workflow.md)
* [Production Environment](/docs/pouta.md)
* [CI/CD Pipeline](/docs/ci-cd.md)
* [Code Quality](/docs/code_quality.md)

### Backlogs 

* [Product Backlog](https://github.com/orgs/HelsinkiUniCollab/projects/1)

#### Sprints
* [Sprint 0 Backlog](https://github.com/orgs/HelsinkiUniCollab/projects/1/views/1)
  * [Burndown Chart](https://github.com/HelsinkiUniCollab/WeatherBasedRecommender/assets/1563603/d7125033-704a-41aa-962c-ccf38f6ffbe8)
* [Sprint 1 Backlog](https://github.com/orgs/HelsinkiUniCollab/projects/1/views/5)
  * [Burndown Chart](https://user-images.githubusercontent.com/1563603/246382227-caa3c55d-8ae1-4ff1-adc4-37d175eda30c.png)
* [Sprint 2 Backlog](https://github.com/orgs/HelsinkiUniCollab/projects/1/views/8)
  * [Burndown Chart](https://github.com/HelsinkiUniCollab/WeatherBasedRecommender/assets/70194087/99774edb-e132-4ed0-831b-e9b7d638ef05)




