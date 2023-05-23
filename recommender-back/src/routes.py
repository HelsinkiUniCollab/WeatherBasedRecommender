from app import app
from flask import jsonify
import apis.weather as weather


@app.route('/', methods=['GET'])
def index():
    """
    Handler for the root endpoint.

    Returns:
        A JSON response containing a greeting message.

    """
    data = {
        'message': 'Hello from the backend!',
        'status': 200
    }
    return jsonify(data)


@app.route('/api/weather', methods=['GET'])
def get_weather():
    """
    Handler for the '/api/weather' endpoint.

    Returns:
        The weather data if errors have not occured.

    """
    return weather.get_weather()


@app.errorhandler(404)
def not_found_error(error):
    """
    Error handler for the 404 (Not Found) error.
    """
    error_data = {
        'message': 'Resource not found',
        'status': error.code
    }
    return jsonify(error_data), 404


@app.errorhandler(500)
def internal_error(error):
    """
    Error handler for the 500 (Internal Server Error) error.
    """
    error_data = {
        'message': 'Internal server error',
        'status': error.code
    }
    return jsonify(error_data), 500
