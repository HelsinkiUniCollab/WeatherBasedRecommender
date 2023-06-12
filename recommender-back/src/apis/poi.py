import json
from apis import weather
from apis import helpers
import requests
import json


#Todo: give category as a parameter to get more accurate data.

def get_pois(category=None):
    if category is None:
        category = ['open_air_water', 'fitness_parks']
    paths = [
        f"src/apis/poi_data/sports_and_physical/water_sports/{category[0]}.json",
        f"src/apis/poi_data/sports_and_physical/outdoor_sports/neighborhood_sports/{category[1]}.json"
        ]
    return merge_json(paths)
def get_pois_as_json(accessibility = False, time=None):
    """
    Retrieves points of interest (POIs) from a JSON file and enriches them with current weather data.

    Returns:
        str: JSON string containing the POIs with weather information.

    Raises:
        KeyError: If an error occurs while processing the data.

    """
    try:
        data = get_pois()

        print("success")
        weatherdata = weather.get_current_weather()
        url = 'http://127.0.0.1:5000/api/forecast'  # Replace with the desired website URL
        response = requests.get(url)
        print("success")
        forecastdata = response.json()
        updated_data = []
        for item in data:
            item = find_nearest_stations_weather_data(weatherdata, forecastdata, item)
            print("success")
            if accessibility not in item["accessibility_shortcoming_count"]:
                updated_data.append(item)
        return json.dumps(updated_data)
    except KeyError as error:
        return {
            'message': 'An error occurred',
            'status': 500,
            'error': str(error)
        }
    
def get_closest_poi_coordinates_data(coordinates, data):
    returned_data = {}
    for hour in data:
        returned_data[hour] = {}
    pois = get_pois()
    closest_coordinates = {}
    for poi in pois:
        smallest, nearest = float('inf'), ''
        lat = float(poi['location']['coordinates'][1])
        lon = float(poi['location']['coordinates'][0])
        for coordinate in coordinates:
            dist = abs(coordinate[0] - lon)\
            + abs(coordinate[1] - lat)
            if dist < smallest:
                smallest, nearest = dist, coordinate
        closest_coordinates[(f"({nearest[0]}, {nearest[1]})")] = f"{lat}, {lon}"
        for hour in data:
            for key, value in closest_coordinates.items():
                fore = data[hour][key]
                returned_data[hour][f"{value}"] = weather.parse_forecast(fore)
    return returned_data


def find_nearest_stations_weather_data(weatherdata, forecastdata, item):
    """
    Finds the nearest weather station to a given POI and adds its weather data to the POI.

    Args:
        weatherdata (dict): A dictionary containing weather data for different stations.
        item (dict): The POI for which weather data needs to be added.

    Returns:
        dict: The modified POI with weather information.

    """
    lat = float(item['location']['coordinates'][1])
    lon = float(item['location']['coordinates'][0])
    smallest, nearest = float('inf'), ''
    for station in weatherdata:
        dist = abs(weatherdata[station]['Longitude'] - lon)\
            + abs(weatherdata[station]['Latitude'] - lat)
        if dist < smallest:
            smallest, nearest = dist, station
    item['weather'] = {}
    item['weather']["current"] = weatherdata[nearest]
    for hour in forecastdata:
        data = forecastdata[hour]
        item["weather"][f'{hour[11:16]}'] = data[f"{lat}, {lon}"]
    return item

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

def add_score_to_poi(item):
    """
    Adds a score to the POI data.
    Args:
        item (dict): The POI for which the score needs to be added.

    Returns:
        dict: The modified POI with the score.

    """
    poi = helpers.PointOfInterest(**item)
    item['score'] = poi.score
    return item