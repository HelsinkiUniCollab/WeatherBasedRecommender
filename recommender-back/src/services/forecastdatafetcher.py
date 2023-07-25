"""
This module provides functionality for fetching forecast and current weather data
using the Finnish Meteorological Institute's open data interface.
"""
from typing import Dict
from fmiopendata.wfs import download_stored_query


class ForecastDataFetcher:
    """
    This class provides methods for fetching forecast and current weather data
    using the Finnish Meteorological Institute's open data interface.
    """

    def get_forecast_data(
        self, start: str, end: str, bbox: str, timestep: int, parameters: str
    ) -> Dict:
        """
        Fetches forecast data for a specified time range, area, timestep and parameters.

        Args:
            start (str): The start time of the forecast period in ISO format.
            end (str): The end time of the forecast period in ISO format.
            bbox (str): Bounding box for the forecast area in format "xmin,ymin,xmax,ymax".
            timestep (int): The timestep in minutes for the forecast data.
            parameters (str): Comma-separated list of parameters to fetch.

        Returns:
            dict: A dictionary containing the forecast data.
        """
        forecast_data = download_stored_query(
            "fmi::forecast::harmonie::surface::grid",
            args=[
                f"starttime={start}",
                f"endtime={end}",
                f"bbox={bbox}",
                f"timestep={timestep}",
                f"parameters={parameters}",
            ],
        )
        return forecast_data

    def get_current_weather_data(self, bbox: str, timeseries: bool) -> Dict:
        """
        Fetches current weather data for a specified area and timeseries.

        Args:
            bbox (str): Bounding box for the forecast area in format "xmin,ymin,xmax,ymax".
            timeseries (bool): Whether to fetch data as a time series or not.

        Returns:
            dict: A dictionary containing the current weather data.
        """
        current_weather_data = download_stored_query(
            "fmi::observations::weather::multipointcoverage",
            args=[
                f"bbox={bbox}",
                f"timeseries={timeseries}",
            ],
        )
        return current_weather_data
