import os
import json
import requests
from requests import Timeout
from .current import Current
from .poi import PointOfInterest
from ..services.data_fetcher import DataFetcher
from ..db.db import get_collection

def get_simulated_pois_as_json(air_temperature, wind_speed, humidity,
                                              precipitation, cloud_amount, air_quality, current_time, sunrise, sunset):
    """
    Retrieves points of interest (POIs) from a JSON file and enriches them with simulated weather data.

    Returns:
        str: JSON string containing the POIs with calculated scores.

    Raises:
        KeyError: If an error occurs while processing the data.
    """
    try:
        pois = get_pois()
        updated_data = []
        for poi in pois:
            poi.set_simulated_weather(air_temperature, wind_speed, humidity,
                                            precipitation, cloud_amount, air_quality)
            poi.calculate_score(current_time, sunrise, sunset)
            updated_data.append(poi.get_json())
        return json.dumps(updated_data)
    except KeyError as error:
        return {"message": "An error occurred", "status": 500, "error": str(error)}
    except Timeout as error:
        return {"message": "Forecast timed out", "status": 500, "error": str(error)}


def get_pois_as_json(category="All"):
    """
    Retrieves points of interest (POIs) from MongoDB and enriches them with current weather data.

    Returns:
        str: JSON string containing the POIs with weather information.

    Raises:
        KeyError: If an error occurs while processing the data.
    """
    try:
        pois = get_pois()
        weather_fetcher = DataFetcher()
        current = Current(weather_fetcher)
        url_fore = os.environ.get("REACT_APP_BACKEND_URL") + "/api/forecast"
        response_fore = requests.get(url_fore, timeout=1200)
        response_fore.raise_for_status()
        forecast_data = response_fore.json()
        url_aqi = os.environ.get("REACT_APP_BACKEND_URL") + "/api/aqi/"
        response_aqi = requests.get(url_aqi, timeout=1200)
        response_aqi.raise_for_status()
        aqi_data = response_aqi.json()
        aqi_data = _replace_datetime_in_aqi_data(forecast_data, aqi_data)
        forecast_data = _add_aqi_to_forecast(forecast_data, aqi_data)
        updated_data = []
        for poi in pois:
            if category not in poi.categories:
                continue
            poi: PointOfInterest = current.find_nearest_stations_weather_data(poi)
            poi = find_nearest_coordinate_forecast_data(poi, forecast_data)
            poi.calculate_score()
            updated_data.append(poi.get_json())
        return json.dumps(updated_data)
    except KeyError as error:
        return {"message": "An error occurred", "status": 500, "error": str(error)}
    except Timeout as error:
        return {"message": "Forecast timed out", "status": 500, "error": str(error)}


def find_nearest_coordinate_forecast_data(poi: PointOfInterest, forecast_data):
    """
    Retrieves all points of interest (POIs) from JSON files and merges them together.

    Args:
        category (list): List of categories of POIs to retrieve. If None, default categories will be used.

    Returns:
        list: List of all POIs.
    """
    try:
        lat = poi.latitude
        lon = poi.longitude
        coord_key = f"{lat}, {lon}"
        for hour in forecast_data:
            data = forecast_data[hour]
            if forecast_data is None or coord_key not in data:
                return poi

            time_key = f"{hour[11:16]}"
            poi.weather[time_key] = data[coord_key]
    except TypeError:
        print("Failed to find nearest coordinate forecast data. TypeError occurred.")

    return poi

def get_pois():
    """
    Fetches and converts mongoDB documents into POI -objects.

    Args:
        test (bool): A flag to indicate if the test environment is used.

    Returns:
        list: List of POI -objects.
    """
    collection = get_collection()
    all_documents = collection.find({})
    pois = []
    for poi in all_documents:
        poi = PointOfInterest(poi['name'], poi['latitude'], poi['longitude'],
                            poi['not_accessible_for'], poi['categories'])
        pois.append(poi)
    return pois

def _add_aqi_to_forecast(forecast_data, aqi_data):
    for datetime, poi_coords in aqi_data.items():
        if datetime in forecast_data:
            for poi_coord, air_quality in poi_coords.items():
                aqi_value = air_quality['Air Quality Index']
                forecast_data[datetime][poi_coord]['Air quality'] = f'{aqi_value} AQI'
    return forecast_data

def _replace_datetime_in_aqi_data(forecast_data, aqi_data):
    """Replaces the date in aqidata to compensate for different caching times

    Args:
        forecast_data (str): forecast_data in json formant
        aqi_data (str): aqi_data in json format

    Returns:
        str: aqi_data with updated datetimes
    """
    updated_aqi_data = {}
    for forecast_datetime, _ in forecast_data.items():
        for aqi_datetime, _ in aqi_data.items():
            updated_aqi_data[aqi_datetime] = aqi_data[forecast_datetime]
    return updated_aqi_data
