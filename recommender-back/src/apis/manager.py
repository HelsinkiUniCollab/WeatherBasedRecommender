import os
import json
import requests
from requests import Timeout
from .models import Poi
from .current import Current
from .poi import PointOfInterest


def get_pois_as_json(accessibility=False):
    '''
    Retrieves points of interest (POIs) from a JSON file and enriches them with current weather data.

    Returns:
        str: JSON string containing the POIs with weather information.

    Raises:
        KeyError: If an error occurs while processing the data.
    '''
    try:
        pois = get_pois()
        current = Current()
        url = os.environ.get('REACT_APP_BACKEND_URL') + '/api/forecast'
        response = requests.get(url, timeout=180)
        forecast_data = response.json()
        updated_data = []
        for poi in pois:
            poi: PointOfInterest = current.find_nearest_stations_weather_data(
                poi)
            poi = find_nearest_coordinate_forecast_data(poi, forecast_data)
            poi.calculate_score()
            if accessibility in poi.not_accessible_for:
                continue
            updated_data.append(poi.get_json())
        return json.dumps(updated_data)
    except KeyError as error:
        return {
            'message': 'An error occurred',
            'status': 500,
            'error': str(error)
        }
    except Timeout as error:
        return {
            'message': 'Forecast timed out',
            'status': 500,
            'error': str(error)
        }


def find_nearest_coordinate_forecast_data(poi: PointOfInterest, forecast_data):
    '''
    Retrieves all points of interest (POIs) from JSON files and merges them together.

    Args:
        category (list): List of categories of POIs to retrieve. If None, default categories will be used.

    Returns:
        list: List of all POIs.
    '''
    lat = poi.latitude
    lon = poi.longitude
    for hour in forecast_data:
        data = forecast_data[hour]
        poi.weather[f'{hour[11:16]}'] = data[f'{lat}, {lon}']
    return poi

def get_pois(test=False):
    '''
    Converts mongoDB documents into POI -objects.

    Args:
        data (list): A list of all poi documents.

    Returns:
        list: List of POI -objects.
    '''
    collection = Poi.get_all(test)
    pois = []
    for poi in collection:
        name = poi['name']
        latitude = poi['latitude']
        longitude = poi['longitude']
        not_accessible_for = poi['not_accessible_for']
        categories = poi['categories']
        poi = PointOfInterest(name, latitude, longitude,
                                  not_accessible_for, categories)
        pois.append(poi)
    return pois
