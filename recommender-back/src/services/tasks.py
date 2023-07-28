"""
tasks.py

This module contains scheduled tasks that update weather forecast
and current weather data periodically.

The `update_forecast_data` function is responsible for updating forecast data
and saving it in cache. It fetches the forecast data from the API, processes it,
and updates the cache.

The `get_current_weather_data` function fetches the current weather data from the API
and updates it in cache.
"""
from src.apis.forecast import Forecast
from src.apis import manager
from src.apis.current import Current
from src.services.forecastdatafetcher import DataFetcher
from src.app import cache

weather_fetcher = DataFetcher()


def get_current_weather_data():
    """
    Fetches the current weather data from the API, processes it and updates the cache.

    The function creates a `Current` object using `weather_fetcher`, gets the current weather
    and stores it in cache.
    """
    current = Current(weather_fetcher)
    current.get_current_weather()
    cache.set("current_weather_data", current.weather)
    print("Current weather data successfully updated.")


def update_forecast_data():
    """
    Fetches the latest forecast data from the API, processes it and updates the cache.

    The function creates a `Forecast` object using `weather_fetcher`, updates the data,
    gets the points of interest,
    gets the data for the closest points of interest and updates the cache.
    """
    forecast = Forecast(weather_fetcher)
    forecast.update_data()
    pois = manager.get_pois()
    poi_forecast = forecast.get_closest_poi_coordinates_data(pois)
    cache.set("forecast_data", poi_forecast)
    print("Forecast data successfully updated.")
