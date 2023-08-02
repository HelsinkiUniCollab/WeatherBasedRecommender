import os
import copy
import json
import requests
from requests import Timeout
from .current import Current
from .poi import PointOfInterest
from ..services.data_fetcher import DataFetcher


def get_pois_as_json(accessibility=False, category="All"):
    """
    Retrieves points of interest (POIs) from a JSON file and enriches them with current weather data.

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
            if category not in poi.categories:
                continue
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
    Retrieves all points of interest (POIs) from JSON files and merges them together.

    Args:
        category (list): List of categories of POIs to retrieve. If None, default categories will be used.

    Returns:
        list: List of all POIs.

    """
    with open("src/static/pois.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        pois = iterate_items(data, [])
        return filter_duplicates(pois)


def filter_duplicates(pois):
    """
    Filters duplicates from POI -list. Some POIs belong to multiple categories which can lead to duplicates.add()

    Args:
        pois (list): List of POIs iterated from file.

    Returns:
        list: Dictionary converted to list containing filtered POIs.

    """
    uniques = {}
    for poi in pois:
        name = poi.name
        if name not in uniques:
            uniques[name] = poi
    return list(uniques.values())


def iterate_items(data, categories):
    """
    Recursively iterates over the data and constructs a list of PointOfInterest objects.

    Args:
        data (list or dict): The data to iterate over.
        categories (list): The list of categories associated with the current data level.

    Returns:
        list: List of PointOfInterest objects constructed from the data.

    """
    pois = []
    if isinstance(data, list):
        for item in data:
            name = item["name"]["fi"]
            longitude = item["location"]["coordinates"][0]
            latitude = item["location"]["coordinates"][1]
            not_accessible_for = list(item["accessibility_shortcoming_count"].keys())
            poi = PointOfInterest(
                name, latitude, longitude, not_accessible_for, categories
            )
            pois.append(poi)
    else:
        for key, item in data.items():
            categories.append(key)
            pois.extend(iterate_items(item, copy.deepcopy(categories)))
            categories.pop()
    return pois
