# Weather-Based Recommender

The purpose of this project is to develop an application that provides users with personalized recommendations for points of interest and routes in Helsinki. It takes into consideration the current weather conditions to enhance the generated suggestions. This application is being created as part of the software engineering course at the [University of Helsinki](https://www.helsinki.fi/fi).

Application can be accessed here: [Weather-Based Recommender](http://128.214.253.51:3000/)

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
* [Definition of Done](/docs/dod.md)
* [Git Workflow](/docs/git-workflow.md)
* [Production Environment](/docs/pouta.md)
* [CI/CD Pipeline](/docs/ci-cd.md)

### Backlogs 

* [Product Backlog](https://github.com/orgs/HelsinkiUniCollab/projects/1)
* [Sprint 0 Backlog](https://github.com/orgs/HelsinkiUniCollab/projects/1/views/1)



