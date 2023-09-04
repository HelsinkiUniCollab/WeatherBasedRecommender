

![ezgif-4-af3762fc40](https://github.com/HelsinkiUniCollab/WeatherBasedRecommender/assets/101641412/fd68b750-12f0-4746-8067-dc073afa5ffe)

[![CI](https://github.com/HelsinkiUniCollab/WeatherbasedRecommender/actions/workflows/ci.yml/badge.svg)](https://github.com/HelsinkiUniCollab/WeatherbasedRecommender/actions/workflows/ci.yml)
[![CD](https://github.com/HelsinkiUniCollab/WeatherbasedRecommender/actions/workflows/cd.yml/badge.svg?branch=main)](https://github.com/HelsinkiUniCollab/WeatherbasedRecommender/actions/workflows/cd.yml)
[![Codecov](https://codecov.io/github/HelsinkiUniCollab/WeatherBasedRecommender/branch/main/graph/badge.svg?token=RU4KTLCO85)](https://codecov.io/github/HelsinkiUniCollab/WeatherBasedRecommender)

The purpose of this project is to develop an application that provides users with personalized recommendations for points of interest and routes in Helsinki. It takes into consideration the current and forecasted weather conditions to enhance the generated suggestions. Read more about [the features of the application](/docs/features.md).

Application can be accessed here: [Weather-Based Recommender](http://128.214.253.51:3000/)

Video introduction of the project: [Part 1](https://www.youtube.com/watch?v=XcDnT0qbQh8) | [Part 2](https://www.youtube.com/watch?v=uWbicdil9OU)

This application is being created as part of the software [engineering course](https://github.com/HY-TKTL/TKT20007-Ohjelmistotuotantoprojekti/) at the [University of Helsinki](https://www.helsinki.fi/fi).

[License](/LICENSE)

## Instructions

```bash
# Give permissions for a script to specify the backend URL
$ chmod +x generate_local_env.sh

# Replace the ellipsis inside the single quotes with your MongoDB development URL
$ ./generate_local_env.sh '...' 

# Start the frontend and backend services on ports 5000 and 3000, respectively
$ docker compose up
```

To get the MongoDB development URL, read more [here](/docs/database.md). To run the frontend and backend services individually, refer to the instructions provided in the [frontend](/recommender-front/README.md) and [backend](/recommender-back/README.md) README's respectively.

## Documentation

* [Features](/docs/features.md)
* [CI/CD Pipeline](/docs/ci-cd.md)
* [Working hours](/docs/hours.md)
* [Team roles](/docs/roles.md)
* [Definition of Done](/docs/dod.md)
* [Git Workflow](/docs/workflow.md)
* [Production Environment](/docs/pouta.md)
* [Databases](/docs/database.md)
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
* [Sprint 3 Backlog](https://github.com/orgs/HelsinkiUniCollab/projects/1/views/9)
  * [Burndown Chart](https://github.com/HelsinkiUniCollab/WeatherBasedRecommender/assets/1563603/82793050-3a47-4eb5-afba-fa1915a7f434)
* [Sprint 4 Backlog](https://github.com/orgs/HelsinkiUniCollab/projects/1/views/10)
  * [Burndown Chart](https://user-images.githubusercontent.com/1563603/259169990-35e11d1b-e03e-4a3c-97b9-a3edcca6b371.png)
* [Sprint 5 Backlog](https://github.com/orgs/HelsinkiUniCollab/projects/1/views/11)
  * [Burndown Chart](https://user-images.githubusercontent.com/1563603/262408124-398195a7-7e9f-49d7-b0be-09ac079ae185.png)




