import overpy
from flask import jsonify

api = overpy.Overpass()

def build_list(nodes):
    """
    Builds a filtered list of POI nodes.
    
    Args:
        nodes (overpy Node): A dictionary of POI nodes.

    Returns:
        List of filtered POI nodes.
    """
    filtered = []
    for node in nodes:
        if 'name' in node.tags:
            node.tags['id'] = node.id
            node.tags['lat'] = float(node.lat)
            node.tags['lon'] = float(node.lon)
            filtered.append(node.tags)
    return filtered

def get_poi_data():
    """
    Fetches POI data from overpass API

    Returns:
        JSON response containing all information related to a POI node

    Raises:
        Exception: If an error occurs during the retrieval process.
    """
    query = """
            (
            node(around:1000,60.2049,24.9649)["tourism"];
            node(around:1000,60.2049,24.9649)["leisure"];
            );
            out;"""

    try:
        result = api.query(query)
    except Exception as error:
        error_data = {
            'message': 'POI query error',
            'status': 500,
            'error': str(error)
        }
        return jsonify(error_data), 500

    data = build_list(result.nodes)
    return jsonify(data)
