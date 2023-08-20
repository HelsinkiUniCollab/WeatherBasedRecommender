# Recommender Backend

This is a Python Flask application for the API's used in Weather-Based Recommender application. Before running, make sure you have generated a `.env` -file, instructions given in the [README.md](/README.md). You also need to have [Poetry](https://python-poetry.org) installed.

## Instructions

```bash
# Navigate to the right project folder
$ cd recommender-back

# Install dependencies using Poetry
$ poetry install
```
Creates a virtual environment and install all the required dependencies defined in the `pyproject.toml` -file.

### Usage
```bash
# Start the Flask development server
$ poetry run invoke start
```
The Flask server will start running, and you can access the API at http://localhost:5000/.

```bash
# Run the tests
$ poetry run invoke test

# Run the code validators
$ poetry run invoke pylint
```

### Docker

```bash 
# Build image
$ docker build -t recommender-backend .

# Run container from image
$ docker run -p 5000:5000 recommender-backend
```

## API Endpoints

Here are some of the API endpoints which the Weather-Based Recommender application uses:
### Forecast Data
```bash
URL: /api/forecast
Method: GET
Description: Response contains weather data with hourly cycles,
  including the timestamp, coordinates, and corresponding values for
  various parameters such as air temperature, wind speed, air pressure,
  and humidity.
```

### Point of Interest Data
```bash
URL: /api/poi
Method: GET
Description: Response contains the all the point-of-interest data with the weather data.
```

### Pathing Data
```bash
URL: /api/path
Method: GET
Example usage: /api/path?start=60.172808,24.909591&end=60.204516,24.962033
Description: Response contains points that form a path based on given coordinates.
```

### Weather Warning
```bash
URL: /api/warning
Method: GET
Description: Response contains Boolean value if the weather is too stormy to suggest any recommendations.
```