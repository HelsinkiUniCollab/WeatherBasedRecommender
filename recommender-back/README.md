# Recommender Backend

Python Flask application for API's used for weather-based recommendations.

## Installation

```bash
# Navigate to the right project folder
$ cd recommender-back

# Install dependencies using Poetry
$ poetry install
```
Creates a virtual environment and install all the required dependencies defined in the pyproject.toml file.

## Usage
```bash
# Activate the virtual environment:
$ poetry shell

# Start the Flask development server:
$ flask run
```
The Flask server will start running, and you can access the API at http://localhost:5000/.

## Testing
```bash
# Run command inside the virtual enviroment
$ pytest
```

## Running in a Docker container

```bash 
# Build image
$ docker build -t recommender-backend .

# Run container from image
$ docker run -p 5000:5000 recommender-backend
```

## API endpoints

### Endpoint 1

URL: /
Method: GET
Description: Shows 'Hello from the backend!' with statuscode 200
