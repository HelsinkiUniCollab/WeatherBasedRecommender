import os
import requests

class InternalApiService:
    """
    Provides methods to fetch data from an internal API.

    This class encapsulates methods to fetch forecast and Air Quality Index (AQI) data from
    an internal API using HTTP requests.

    Attributes:
        BASE_URL (str): The base URL of the internal API.
        TIMEOUT (int): The timeout duration for HTTP requests in seconds.

    Note:
    - The BASE_URL is obtained from the 'REACT_APP_BACKEND_URL' environment variable.
    - The TIMEOUT value can be adjusted as needed.
    """

    BASE_URL = os.environ.get("REACT_APP_BACKEND_URL")
    TIMEOUT = 1200

    @classmethod
    def fetch_forecast(cls):
        """
        Fetches forecast data from the internal API.

        Returns:
            dict: Forecast data in JSON format.

        Raises:
            requests.exceptions.RequestException: If the HTTP request to the API fails.
        """
        url = f"{cls.BASE_URL}/api/forecast"
        response = requests.get(url, timeout=cls.TIMEOUT)
        response.raise_for_status()
        return response.json()

    @classmethod
    def fetch_aqi(cls):
        """
        Fetches Air Quality Index (AQI) data from the internal API.

        Returns:
            dict: AQI data in JSON format.

        Raises:
            requests.exceptions.RequestException: If the HTTP request to the API fails.
        """
        url = f"{cls.BASE_URL}/api/aqi"
        response = requests.get(url, timeout=cls.TIMEOUT)
        response.raise_for_status()
        return response.json()
