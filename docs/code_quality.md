# Code Quality

Linting is used to ensure the project maintains high-quality coding standards.

## Backend

The backend uses Pylint. The rules can be found in the [.pylintrc](https://github.com/HelsinkiUniCollab/WeatherbasedRecommender/blob/main/recommender-back/.pylintrc) file.

```bash
# Run the Pylint validators
$ poetry run invoke pylint
```

## Frontend

The frontend uses ESLint and follows [Airbnb's rules](https://github.com/airbnb/javascript).

```bash
# Check the linting
$ npm run lint

# Fix most of the linting issues
$ npm run lint:fix
```
