"""
This module defines the routes for the application's Flask server.
It includes endpoints for fetching forecast data, point of interest (POI) data, 
accessible POI data and current weather data for Helsinki Kaisaniemi. 
Additionally, it contains error handlers for 404 (Not Found) and 500 (Internal Server Error) errors.
"""

from flask import jsonify
from .app import app, cache
from .apis.current import Current
from .apis import manager
from .services.forecastdatafetcher import DataFetcher

weather_fetcher = DataFetcher()


@app.route("/", methods=["GET"])
def index():
    """
    Handler for the root endpoint.

    Returns:
        A JSON response containing a greeting message.

    """
    data = {"message": "Hello from the backend!", "status": 200}
    return jsonify(data)


@app.route("/api/forecast", methods=["GET"])
def get_forecast():
    """
    Handler for the '/api/forecast' endpoint.

    Returns:
        Forecast for the POI's.
    """
    poi_forecast = cache.get("forecast_data")
    if not poi_forecast:
        return jsonify({"message": "Forecast data not available yet"})

    return jsonify(poi_forecast)


@app.route("/api/poi/", methods=["GET"])
def get_poi_data():
    """
    Handler for the '/api/poi' endpoint.

    Returns:
        Poi data if errors have not occurred.
    """
    return manager.get_pois_as_json()


@app.route("/api/poi/<accessibility>", methods=["GET"])
def get_poi_acessible_poi_data(accessibility):
    """
    Handler for the '/api/poi' endpoint.

    Returns:
        Poi data if errors have not occurred.
    """
    return manager.get_pois_as_json(accessibility)


@app.route("/api/weather", methods=["GET"])
def get_weather_helsinki_kaisaniemi():
    """
    Handler for the /api/weather endpoint.

    Returns:
        Current weather data for Helsinki Kaisaniemi.
    """
    current = cache.get("current_weather_data")
    helsinki_kaisaniemi = current.get("Helsinki Kaisaniemi")
    return jsonify(helsinki_kaisaniemi)


@app.errorhandler(404)
def not_found_error(error):
    """
    Error handler for the 404 (Not Found) error.
    """
    error_data = {"message": "Resource not found", "status": error.code}
    return jsonify(error_data), 404


@app.errorhandler(500)
def internal_error(error):
    """
    Error handler for the 500 (Internal Server Error) error.
    """
    error_data = {"message": "Internal server error", "status": error.code}
    return jsonify(error_data), 500
