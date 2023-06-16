# Recommender Backend

Python Flask application for API's used for weather-based recommendations.

## Instructions

```bash
# Navigate to the right project folder
$ cd recommender-back

# Install dependencies using Poetry
$ poetry install
```
Creates a virtual environment and install all the required dependencies defined in the pyproject.toml file.

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

### Endpoint for backend health

```bash
URL: /
Method: GET
Description: Shows 'Hello from the backend!' with statuscode 200
```

### Endpoint for Weather and Forecast data
```bash
URL: /api/forecast
Method: GET
Description: Response contains weather data with hourly cycles,
  including the timestamp, coordinates, and corresponding values for
  various parameters such as air temperature, wind speed, air pressure,
  and humidity in JSON.

```

### Endpoint for Point of Interest data
```bash
URL: /api/poi
Method: GET
Description: Response contains the all the point-of-interest data as JSON
```


