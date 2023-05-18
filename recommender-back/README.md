# Recommender Backend

Python Flask application for api's used for Weather-based Recommendations.

## Installation

1. Navigate to the right project folder

`cd recommender-back`

2. Install dependencies using Poetry

`poetry install`
Creates a virtual environment and install all the required dependencies defined in the pyproject.toml file.

## Usage

1. Activate the virtual environment:
`poetry shell`

2. Start the Flask development server:
`flask run`

The Flask server will start running, and you can access the API at http://localhost:5000/.

## Testing

1. Run command inside virtual enviroment
`pytest`

## API endpoints

### Endpoint 1:

URL: /
Method: GET
Description: Shows 'Hello from the backend!' with statuscode 200.
