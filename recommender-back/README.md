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
  and humidity in JSON. Only contains the wanted coords from the grid to
  match selected pois.

```

### Endpoint for Point of Interest data
```bash
URL: /api/poi
Method: GET
Description: Response contains the all the point-of-interest data as JSON
```

## Example flow of @app.route/api/poi route
```
|
|-- Call 'get_poi_data' Flask route
|   |
|   |-- Call 'get_pois_as_json' function
|   |   |
|   |   |-- Call 'get_pois' function
|   |   |   |-- Fetch POIs from JSON files
|   |   |
|   |   |-- Call 'weather.get_current_weather' function
|   |   |   |-- Fetch current weather data from weather stations
|   |   |
|   |   |-- Call 'get_forecast' Flask route
|   |   |   |-- Fetch forecast data from api/forecast
|   |   |  
|   |   |-- Call 'find_nearest_stations_weather_data' function for each POI
|   |   |   |-- Find nearest weather station for the POI
|   |   |   |   |-- Calculate distance between POI and weather station
|   |   |   |   |   |-- Iterate over weather stations
|   |   |   |-- Add weather data to the POI
|   |   |
|   |   |-- Call 'add_forecast_to_poi' function for each POI
|   |   |   |-- Add forecast to poi
|   |   |   |   |-- Iterate over forecast data
|   |   |   |-- Add forecast data to the POI by coordinates associated with them
|   |   |
|   |   |-- Filter POIs based on accessibility
|   |   |
|   |   |-- Create Recommender object for each POI
|   |   |
|   |   |-- Calculate scores for each POI timestep based on weather conditions now and in forecast
|   |   |
|   |   |-- Convert POI data to JSON string
|   |
|   |-- Return POI data as JSON response
|
```

## Example flow of @app.route/api/forecast route

```
|
|-- Call 'get_forecast' Flask route
|
|-- Check cache for cached forecast data
|   |-- If cached data exists and is valid
|   |   |-- Return cached forecast data
|
|-- If cached data does not exist or is invalid
|   |-- Create a new ForecastGrid object
|   |   |-- Initialize a new ForecastGrid object
|   |
|   |-- Update data in the ForecastGrid object
|   |   |-- Get current, start, and end times for the forecast
|   |   |-- Define the bounding box for the forecast coordinates
|   |   |-- Set the time step for the forecast
|   |   |-- Query the forecast data for the specified parameters
|   |   |-- Extract the latest forecast data from the retrieved data
|   |   |-- Parse and store the forecast data in the ForecastGrid object
|   |
|   |-- Get coordinates from the ForecastGrid object
|   |   |-- Retrieve the coordinates from the ForecastGrid object
|   |
|   |-- Get forecast data for closest coordinates to POIs
|   |   |-- Retrieve the list of POIs (points of interest)
|   |   |-- Initialize an empty dictionary to store the closest coordinates for each POI
|   |
|   |   |-- Iterate over each POI
|   |   |   |-- Set initial values for the smallest distance and nearest coordinates
|   |   |   |
|   |   |   |-- Iterate over each coordinate in the given coordinates
|   |   |   |   |-- Calculate the distance between the current coordinate and the POI's latitude and longitude
|   |   |   |   |-- Update the smallest distance and nearest coordinates if the calculated distance is smaller
|   |   |   |
|   |   |   |-- Add the nearest coordinates to the closest_coordinates dictionary
|   |
|   |   |-- Iterate over each hour in the forecast data
|   |   |   |-- Iterate over the closest_coordinates dictionary
|   |   |   |   |-- Get the forecast data for the current hour and coordinates
|   |   |   |   |-- Parse the forecast data using the parse_forecast function from the weather module
|   |   |   |   |-- Add the parsed forecast data to the returned_data dictionary using the POI's coordinates as the key
|   |
|   |-- Convert forecast data to JSON format
|   |   |-- Convert the returned_data dictionary to a JSON string
|   |
|   |-- Cache the forecast data
|   |   |-- Cache the JSON string of forecast data with a timeout of 3600 seconds
|   |
|   |-- Return the forecast data
|   |   |-- Return the JSON string of forecast data
|
```

