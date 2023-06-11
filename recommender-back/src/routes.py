from app import app, cache
from apis import weather
from apis import poi
from flask import jsonify
from flask_caching import Cache


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

@app.route('/api/forecast', methods=['GET'])
@cache.cached(timeout=3600)
def get_forecast():
    forecastgrid = weather.ForecastGrid()
    forecastgrid.update_data()
    return jsonify(forecastgrid.get_data())

@app.route('/api/poi/', methods=['GET'])
def get_poi_data():
    '''
    Handler for the '/api/poi' endpoint.

    Returns:
        Poi data if errors have not occurred.
    '''
    return poi.get_pois_as_json()

@app.route('/api/poi/<accessibility>', methods=['GET'])
def get_poi_acessible_poi_data(accessibility):
    '''
    Handler for the '/api/poi' endpoint.

    Returns:
        Poi data if errors have not occurred.
    '''
    return poi.get_pois_as_json(accessibility)


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
