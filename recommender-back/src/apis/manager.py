from apis.current import Current
from apis.poi import PointOfInterest
import json
import requests
import os
import copy


def get_pois_as_json(accessibility=False, category='All'):
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
        response = requests.get(url)
        forecast_data = response.json()
        updated_data = []
        for poi in pois:
            if category not in poi.categories:
                continue
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


def get_pois():
    '''
    Retrieves all points of interest (POIs) from JSON files and merges them together.

    Args:
        category (list): List of categories of POIs to retrieve. If None, default categories will be used.

    Returns:
        list: List of all POIs.

    '''
    categories = []
    with open('src/static/pois.json', 'r') as file:
        data = json.load(file)
        return iterate_items(data, categories)


def iterate_items(data, categories):
    '''
    Recursively iterates over the data and constructs a list of PointOfInterest objects.

    Args:
        data (list or dict): The data to iterate over.
        categories (list): The list of categories associated with the current data level.

    Returns:
        list: List of PointOfInterest objects constructed from the data.

    '''
    pois = []
    if type(data) == list:
        for item in data:
            name = item['name']['fi']
            longitude = item['location']['coordinates'][1]
            latitude = item['location']['coordinates'][0]
            not_accessible_for = list(
                item['accessibility_shortcoming_count'].keys())
            poi = PointOfInterest(name, longitude, latitude,
                                  not_accessible_for, categories)
            pois.append(poi)
    else:
        for key, item in data.items():
            categories.append(key)
            pois.extend(iterate_items(item, copy.deepcopy(categories)))
            categories.pop()
    return pois
