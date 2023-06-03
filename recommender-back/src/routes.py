from app import app
from apis import weather
import numpy as np
import json
from flask import jsonify


@app.route('/', methods=['GET'])
def index():
    '''
    Handler for the root endpoint.

    Returns:
        A JSON response containing a greeting message.

    '''
    data = {
        'message': 'Hello from the backend!',
        'status': 200
    }
    return jsonify(data)


@app.route('/api/weather', methods=['GET'])
def get_weather():
    '''
    Handler for the '/api/weather' endpoint.

    Returns:
        The weather data if errors have not occurred.

    '''
    return weather.get_full_weather_info()

@app.route('/api/poi', methods=['GET'])
def get_poi_data():
    '''
    Handler for the '/api/poi' endpoint.

    Returns:
        Poi data if errors have not occurred.
    '''
    with open('src/pois.json') as f:
        data = json.load(f)
        weatherdata = weather.get_current_weather()
        for item in data:
            lat = float(item['location']['coordinates'][1])
            lon = float(item['location']['coordinates'][0])
            smallest = float('inf')
            nearest = ''
            for station in weatherdata:
                dist = abs(weatherdata[station]['Longitude'] - lon)\
                    + abs(weatherdata[station]['Latitude'] - lat)
                if dist < smallest:
                    smallest = dist
                    nearest = station
            item['weather'] = weatherdata[nearest]
        return json.dumps(data)


@app.errorhandler(404)
def not_found_error(error):
    '''
    Error handler for the 404 (Not Found) error.
    '''
    error_data = {
        'message': 'Resource not found',
        'status': error.code
    }
    return jsonify(error_data), 404


@app.errorhandler(500)
def internal_error(error):
    '''
    Error handler for the 500 (Internal Server Error) error.
    '''
    error_data = {
        'message': 'Internal server error',
        'status': error.code
    }
    return jsonify(error_data), 500
