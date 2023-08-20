import os
import requests

class InternalApiService:

    BASE_URL = os.environ.get("REACT_APP_BACKEND_URL")
    TIMEOUT = 1200

    @classmethod
    def fetch_forecast(cls):
        url = f"{cls.BASE_URL}/api/forecast"
        response = requests.get(url, timeout=cls.TIMEOUT)
        response.raise_for_status()
        return response.json()

    @classmethod
    def fetch_aqi(cls):
        url = f"{cls.BASE_URL}/api/aqi"
        response = requests.get(url, timeout=cls.TIMEOUT)
        response.raise_for_status()
        return response.json()
