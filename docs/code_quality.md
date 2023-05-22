# Code Quality

Linting is used to ensure the project maintains high-quality coding standards.

## Backend

The backend uses Pylint. The rules can be found in the [.pylintrc](https://github.com/HelsinkiUniCollab/WeatherbasedRecommender/blob/main/recommender-back/.pylintrc) file.

Currently, you can only check individual files.

To enter the virtual environment, run the following command:

```bash
poetry shell
```

Then, execute the command:

```bash
pylint file_name.py
```

Replace "file_name.py" with the desired Python file.

## Frontend

The frontend uses ESLint and follows [Airbnb's rules](https://github.com/airbnb/javascript).

To check the linting, run the following command:

```bash
npm run lint
```

If the command doesn't return anything, it means that there are no linting issues.
