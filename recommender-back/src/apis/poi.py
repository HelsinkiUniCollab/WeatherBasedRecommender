from apis import weather
from apis import helpers
import json
import requests
import os


def merge_json(paths):
    """
    Merges json files together.

    Args:
        paths: list of file paths

    Returns:
        List: json files merged together as a list.
    """
    merged = []
    for path in paths:
        with open(path, 'r') as json_file:
            data = json.load(json_file)
            merged = merged + data
    return merged


def get_pois_as_json(accessibility=False, time=None):
    """
    Retrieves points of interest (POIs) from a JSON file and enriches them with current weather data.

    Returns:
        str: JSON string containing the POIs with weather information.

    Raises:
        KeyError: If an error occurs while processing the data.

    """
    try:
        pois = get_pois()
        weather_data = weather.get_current_weather()
        url = os.environ.get('REACT_APP_BACKEND_URL') + '/api/forecast'
        response = requests.get(url)
        forecast_data = response.json()
        updated_data = []
        for poi in pois:
            poi = find_nearest_stations_weather_data(poi, weather_data)
            poi = find_nearest_coordinate_forecast_data(poi, forecast_data)
            if accessibility not in poi["accessibility_shortcoming_count"]:
                updated_data.append(poi)
            poi = helpers.Recommender(time, **poi)
        return json.dumps(updated_data)
    except KeyError as error:
        return {
            'message': 'An error occurred',
            'status': 500,
            'error': str(error)
        }


def find_nearest_stations_weather_data(poi, weather_data):
    """
    Finds the nearest weather station to a given point of interest (POI) and adds its weather data to the POI.

    Args:
        poi (dict): The POI for which weather data needs to be added.
        weather_data (dict): A dictionary containing weather data for different weather stations.

    Returns:
        dict: The modified POI with weather information.

    """
    lat = float(poi['location']['coordinates'][1])
    lon = float(poi['location']['coordinates'][0])
    smallest, nearest = float('inf'), ''
    for station in weather_data:
        dist = abs(weather_data[station]['Longitude'] - lon)\
            + abs(weather_data[station]['Latitude'] - lat)
        if dist < smallest:
            smallest, nearest = dist, station
    poi['weather'] = {}
    poi['weather']["Current"] = weather_data[nearest]
    return poi


def find_nearest_coordinate_forecast_data(poi, forecast_data):
    """
    Finds the closest coordinate forecast data to a given point of interest (POI) by the given hour,
    and adds it to the POI.

    Args:
        poi (dict): The POI for which forecast data needs to be added.
        forecast_data (dict): A dictionary containing forecast data for different coordinates.

    Returns:
        dict: The modified POI with forecast information.

    """
    lat = float(poi['location']['coordinates'][1])
    lon = float(poi['location']['coordinates'][0])
    for hour in forecast_data:
        data = forecast_data[hour]
        poi["weather"][f'{hour[11:16]}'] = data[f"{lat}, {lon}"]
    return poi


def get_closest_poi_coordinates_data(coordinates, data):
    """
    Finds the nearest coordinates forecast data for all of the POI's coordinates. Used for caching only
    the nearest coordinates to the POI's.

    Args:
        coordinates (list): List of coordinates for the POI.
        data (dict): A dictionary containing forecast data for different hours and coordinates.

    Returns:
        dict: A dictionary containing the nearest coordinates forecast data for each hour.

    """
    returned_data = {hour: {} for hour in data}
    pois = get_pois()
    closest_coordinates = {}
    for poi in pois:
        smallest = float('inf')
        nearest = []
        lat = float(poi['location']['coordinates'][1])
        lon = float(poi['location']['coordinates'][0])
        for coordinate in coordinates:
            dist = abs(coordinate[0] - lat)\
                + abs(coordinate[1] - lon)
            if dist < smallest:
                smallest = dist
                nearest = [coordinate[0], coordinate[1]]
        closest_coordinates[(
            f"({nearest[0]}, {nearest[1]})")] = f"{lat}, {lon}"
        for hour in data:
            for key, value in closest_coordinates.items():
                forecast = data[hour][key]
                returned_data[hour][f"{value}"] = weather.parse_forecast(
                    forecast)
    return returned_data


def get_pois(category=None):
    """
    Retrieves all points of interest (POIs) from JSON files and merges them together.

    Args:
        category (list): List of categories of POIs to retrieve. If None, default categories will be used.

    Returns:
        list: List of all POIs.

    """
    if category is None:
        category = ['open_air_water', 'fitness_parks']
    paths = [
        f"src/apis/poi_data/sports_and_physical/water_sports/{category[0]}.json",
        f"src/apis/poi_data/sports_and_physical/outdoor_sports/neighborhood_sports/{category[1]}.json"
    ]
    return merge_json(paths)
