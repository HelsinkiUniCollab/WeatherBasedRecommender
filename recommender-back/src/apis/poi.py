import json
from apis import weather

#Todo: give category as a parameter to get more accurate data.

def get_pois_as_json(category=['open_air_water','fitness_parks'], accessibility = False):
    """
    Retrieves points of interest (POIs) from a JSON file and enriches them with current weather data.

    Returns:
        str: JSON string containing the POIs with weather information.

    Raises:
        KeyError: If an error occurs while processing the data.

    """
    paths = [
        f"src/apis/poi_data/sports_and_physical/water_sports/{category[0]}.json",
        f"src/apis/poi_data/sports_and_physical/outdoor_sports/neighborhood_sports/{category[1]}.json"
        ]
    try:
        with open('src/pois.json') as file:
            data = merge_json(paths)
            weatherdata = weather.get_current_weather()
            updated_data = []
            for item in data:
                item = find_nearest_stations_weather_data(weatherdata, item)
                if accessibility not in item["accessibility_shortcoming_count"]:
                    updated_data.append(item)
        return json.dumps(updated_data)
    except KeyError as error:
        return {
            'message': 'An error occurred',
            'status': 500,
            'error': str(error),
        }


def find_nearest_stations_weather_data(weatherdata, item):
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
    item['weather'] = weatherdata[nearest]
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
