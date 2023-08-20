import json
from .config import Config
from flask import jsonify, request
from .app import app, cache
from .apis.aqi import AQI
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
    Handler for the '/api/forecast' endpoint. Caching 1 hour.

    Returns:
        Forecast for the POI's.
    """
    forecast = Forecast(weather_fetcher)
    forecast.update_data()
    pois = manager.get_pois()
    poi_forecast = forecast.get_closest_poi_coordinates_data(pois)
    result = json.dumps(poi_forecast)
    return result


@app.route("/api/aqi/", methods=["GET"])
@cache.cached(timeout=Config.AQI_CACHE_TO)
def get_aqi_forecast():
    """
    Handler for the '/api/aqi' endpoint. Caching 24 hours.

    Returns:
        string: Aqi forecast for the POI's in json format
    """
    aqi = AQI()
    aqi.download_netcdf_and_store()
    pois = manager.get_pois()
    aqi_data = aqi.to_json(pois)
    result = json.dumps(aqi_data)
    return result


@app.route("/api/poi/", methods=["GET"])
def get_poi_data():
    """
    Handler for the '/api/poi' endpoint.

    Returns:
        Poi data if errors have not occurred.
    """
    return manager.get_pois_as_json()
    


@app.route("/api/simulator", methods=["POST"])
def get_simulated_poi_data():
    """
    Handler for the '/api/poi' endpoint.

    Returns:
        Poi data if errors have not occurred.
    """
    data = request.get_json()
    air_temperature = data.get('air_temperature')
    wind_speed = data.get('wind_speed')
    humidity = data.get('humidity')
    precipitation = data.get('precipitation')
    cloud_amount = data.get('cloud_amount')
    air_quality = data.get('air_quality')
    current_time = data.get('current_time')
    sunrise = data.get('sunrise')
    sunset = data.get('sunset')
    if '' in [air_temperature, wind_speed, humidity, precipitation, cloud_amount, air_quality, current_time, sunrise, sunset]:
        return jsonify({"error": "Missing parameters"}), 400
    return manager.get_simulated_pois_as_json(air_temperature, wind_speed, humidity,
                                              precipitation, cloud_amount, air_quality, current_time, sunrise, sunset)


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
        coords = [[coord[1], coord[0]] for coord in route_coordinates]
        return jsonify(coords), 200
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
