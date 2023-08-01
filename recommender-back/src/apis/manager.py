import os
import json
import requests
from requests import Timeout
from .current import Current
from .poi import PointOfInterest
from ..db.models import Poi
from ..db.db import get_collection
from ..services.forecastdatafetcher import DataFetcher
from ..services.poi_init import init_pois


def get_pois_as_json(accessibility=False):
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
        url = os.environ.get("REACT_APP_BACKEND_URL") + "/api/forecast"
        response = requests.get(url, timeout=180)
        forecast_data = response.json()
        updated_data = []
        for poi in pois:
            poi: PointOfInterest = current.find_nearest_stations_weather_data(poi)
            poi = find_nearest_coordinate_forecast_data(poi, forecast_data)
            poi.calculate_score()
            if accessibility in poi.not_accessible_for:
                continue
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
        for hour in forecast_data:
            data = forecast_data[hour]
            time_key = f"{hour[11:16]}"
            coord_key = f"{lat}, {lon}"

            if forecast_data is None or coord_key not in data:
                return poi

            poi.weather[time_key] = data[coord_key]
    except TypeError:
        print("Failed to find nearest coordinate forecast data. TypeError occurred.")

    return poi

def get_pois(test=False):
    """
    Fetches and converts mongoDB documents into POI -objects.

    Args:
        test (bool): A flag to indicate if the test environment is used.

    Returns:
        list: List of POI -objects.
    """
    collection = get_collection()
    if collection.count_documents({}) == 0:
        print('Start POI initialization')
        init_pois()
    all_documents = collection.find({})
    pois = []
    for poi in all_documents:
        poi = PointOfInterest(poi['name'], poi['latitude'], poi['longitude'],
                              poi['not_accessible_for'], poi['categories'])
        pois.append(poi)
    return pois
