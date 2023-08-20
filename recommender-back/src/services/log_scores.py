import json
from ..db.db import get_collection

def save_score_history(data, collection):
    """
    Fetches weather data and scores for pois and saves the data poi by poi to MongoDB.

    Args:
        data (dict): JSON string containing the POIs with weather information.

    Raises:
        KeyError: If an error occurs while processing and saving the data.
    """
    try:
        print("Saving score history")
        collection = get_collection(collection)
        current_db_size_mb = collection.database.command("dbstats")["storageSize"] / (1024 * 1024)
        print(current_db_size_mb)
        if current_db_size_mb >= 500:
            print("Database size too large - deleting older scores")
            oldest_data = collection.find().sort("_id", 1).limit(625)  
            for doc in oldest_data:
                collection.delete_one({"_id": doc["_id"]})
        data_dict = json.loads(data)
        collection.insert_many(data_dict)
        return {"message": "Data saved successfully", "status": 200} 
    except KeyError as error:
        return {"message": "An error occurred", "status": 500, "error": str(error)}
