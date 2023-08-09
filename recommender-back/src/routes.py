import json
from flask import jsonify, request
from .app import app, cache
from .apis.forecast import Forecast
from .apis.current import Current
from .apis.pathing import GreenPathsAPI
from .apis import manager
from .services.data_fetcher import DataFetcher

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
@cache.cached()
def get_forecast():
    """
    Handler for the '/api/forecast' endpoint.

    Returns:
        Forecast for the POI's.
    """
    forecast = Forecast(weather_fetcher)
    forecast.update_data()
    pois = manager.get_pois()
    poi_forecast = forecast.get_closest_poi_coordinates_data(pois)
    return json.dumps(poi_forecast)


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
        POI-data if errors have not occurred.
    """
    return manager.get_pois_as_json(accessibility)


@app.route("/api/simulator", methods=["GET"])
def get_simulated_poi_data():
    """
    Handler for the '/api/poi' endpoint.

    Returns:
        Poi data if errors have not occurred.
    """
    air_temperature = request.args.get('air_temperature')
    wind_speed = request.args.get('wind_speed')
    humidity = request.args.get('humidity')
    precipitation = request.args.get('precipitation')
    cloud_amount = request.args.get('cloud_amount')
    air_quality = request.args.get('air_quality')
    if '' in [air_temperature, wind_speed, humidity, precipitation, cloud_amount, air_quality]:
        return jsonify({"error": "Missing parameters"}), 400
    return manager.get_simulated_pois_as_json(air_temperature, wind_speed, humidity,
                                              precipitation, cloud_amount, air_quality)


@app.route("/api/warning", methods=["GET"])
@cache.cached()
def get_weather_warning():
    """
    Handler for the '/api/warning' endpoint. 

    Returns:
        Boolean according to if there is weather warning.
    """
    current = Current(weather_fetcher)
    warning = current.get_current_weather_warning("Helsinki Kaisaniemi")
    return jsonify(warning)


@app.route('/path', methods=['GET'])
def get_path():
    """
    Handler for the '/api/path' endpoint.

    Returns:
        Coordinates for the route based on request parameters.
    """
    start_coords = request.args.get('start', None)
    end_coords = request.args.get('end', None)

    if not start_coords or not end_coords:
        return jsonify({"error": "Missing start or end coordinates"}), 400

    try:
        start_coords = tuple(map(float, start_coords.split(',')))
        end_coords = tuple(map(float, end_coords.split(',')))
    except ValueError:
        return jsonify({"error": "Invalid coordinates"}), 400

    green_paths = GreenPathsAPI(start_coords, end_coords)
    if route_coordinates := green_paths.route_coordinates:
        return jsonify(route_coordinates), 200
    return jsonify({"error": "Could not fetch route data"}), 500

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
