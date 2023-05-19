from flask import Flask
from fmiopendata.wfs import download_stored_query

app = Flask(__name__)

@app.route('/weather', methods=['GET'])
def index():
    obs = download_stored_query("fmi::observations::weather::multipointcoverage",
                                args=["place=Kumpula,Helsinki"])
    airtemperature = query_handler(obs, "Helsinki Kumpula", "Air temperature")
    
    obs = download_stored_query("urban::observations::airquality::hourly::multipointcoverage",
                                args=["place=Kumpula,Helsinki"])
    airquality = query_handler(obs, "Helsinki Mäkelänkatu", "Air Quality Index")
    return {
        "airtemperature": airtemperature,
        "airquality": airquality
    }

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