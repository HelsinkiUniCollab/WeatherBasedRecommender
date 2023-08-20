import os
import json
import copy
from ..apis.poi import PointOfInterest
from ..db.models import Poi
from ..db.db import get_collection

def init_pois():
    '''
    Retrieves all points of interest (POIs) from JSON file and merges them together.

    Args:
        category (list): List of categories of POIs to retrieve. If None, default categories will be used.

    Returns:
        list: List of all POIs.

    '''
    try:
        print(' * Initiliazing POIs to MongoDB')
        file_path = os.path.join(os.path.dirname(__file__), '..', 'static', 'pois.json')
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            pois = filter_duplicates(iterate_items(data, []))
            for poi in pois:
                Poi.save(Poi(poi.name, poi.latitude, poi.longitude, poi.not_accessible_for, poi.categories))
        return pois
    except FileNotFoundError:
        print(' * Error: pois.json not found.')
    except Exception as e:
        print(f' * Error occurred while initializing POIs: {e}')

def filter_duplicates(pois):
    uniques = {}
    for poi in pois:
        name = poi.name
        if name not in uniques:
            uniques[name] = poi
    return list(uniques.values())

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
    if isinstance(data, list):
        for item in data:
            name = item['name']['fi']
            longitude = item['location']['coordinates'][0]
            latitude = item['location']['coordinates'][1]
            not_accessible_for = list(item['accessibility_shortcoming_count'].keys())
            poi = PointOfInterest(name, latitude, longitude,
                                  not_accessible_for, categories)
            pois.append(poi)
    else:
        for key, item in data.items():
            categories.append(key)
            pois.extend(iterate_items(item, copy.deepcopy(categories)))
            categories.pop()
    return pois

def initialize_collection():
    collection = get_collection('pois')
    if collection.count_documents({}) == 0:
        init_pois()
