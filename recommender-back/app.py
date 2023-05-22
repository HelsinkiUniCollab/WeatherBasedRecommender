from flask import Flask, jsonify
from flask_cors import CORS
from fmiopendata.wfs import download_stored_query

app = Flask(__name__)
CORS(app)

# Custom error handler for 404 - Resource Not Found
@app.errorhandler(404)
def not_found_error(error):
    error_data = {
        'message': 'Resource not found',
        'status': 404
    }
    return jsonify(error_data), 404

# Custom error handler for 500 - Internal Server Error
@app.errorhandler(500)
def internal_error(error):
    error_data = {
        'message': 'Internal server error',
        'status': 500
    }
    return jsonify(error_data), 500

@app.route('/', methods=['GET'])
def index():
    data = {
        'message': 'Hello from the backend!',
        'status': 200
    }
    return jsonify(data)

@app.route('/api/weather', methods=['GET'])
def get_weather():
    try:
        obs = download_stored_query("fmi::observations::weather::multipointcoverage",
                                    args=["place=Kumpula,Helsinki"])
        airtemperature = query_handler(obs, "Helsinki Kumpula", "Air temperature")

        obs = download_stored_query("urban::observations::airquality::hourly::multipointcoverage",
                                    args=["place=Kumpula,Helsinki"])
        airquality = query_handler(obs, "Helsinki Mäkelänkatu", "Air Quality Index")

        data = {
            "airtemperature": airtemperature,
            "airquality": airquality
        }
        return jsonify(data)
    except Exception as e:
        error_data = {
            'message': 'An error occurred',
            'status': 500,
            'error': str(e)
        }
        return jsonify(error_data), 500

def query_handler(obs, station, value):
    while True:
        latest = max(obs.data.keys())
        data = obs.data[latest][station][value]
        data = str(data.get("value"))
        if data in {"nan", "NaN"}:
            obs.data.pop(latest)
            continue
        break
    return data

if __name__ == '__main__':
    app.run(debug=True)