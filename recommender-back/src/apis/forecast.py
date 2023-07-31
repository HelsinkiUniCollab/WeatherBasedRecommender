import math
import time
import errno
import numpy as np
from .times import utc_to_finnish, get_forecast_times
from ..config import Config
from ..services.forecastdatafetcher import DataFetcher


class Forecast:
    def __init__(self, fetcher: DataFetcher):
        self.fetcher = fetcher
        self.data = None
        self.valid_times = None
        self.data_levels = None
        self.coordinates = None

    def update_data(self):
        """
        Updates the forecast data.
        Fetches the latest data and updates class properties if new data is available.
        """
        current, start, end = get_forecast_times()
        print(f"Query for the new Grid object at time: {current} UTC")
        forecast_data = self.get_latest_forecast(start, end)
        latest_forecast = max(forecast_data.data.keys())

        if not self.data or latest_forecast > max(self.data.keys()):
            self.data = forecast_data.data[latest_forecast]
            self.parse_forecast_data()
            self.update_forecast_properties()

    def get_latest_forecast(self, start, end):
        """
        Retrieves the latest forecast data within the specified time range.
        Args:
            start (datetime): The start time for the data retrieval.
            end (datetime): The end time for the data retrieval.
        Returns:
            Grid: The forecast grid data within the specified time range.
        """
        return self.fetcher.get_forecast_data(
            start, end, Config.BBOX, Config.TIMESTEP, Config.PARAMETERS
        )

    def parse_forecast_data(self):
        """
        Parses the forecast data with retry attempts on failure.
        Raises:
            ConnectionResetError: If a ConnectionResetError occurs during parsing after maximum number of retry attempts.
        """
        max_retries = 3
        retry_delay = 5  # delay in seconds

        for attempt in range(max_retries):
            try:
                self.data.parse(delete=True)
                break
            except ConnectionResetError as error:
                if error.errno != errno.ECONNRESET:
                    # Not the error we are looking for, re-raise
                    raise
                print(f"ConnectionResetError during parsing: {error}")
                if attempt < max_retries - 1:
                    time.sleep(retry_delay)
                    print(f"Retrying parsing ({attempt + 1} out of {max_retries})...")
                else:
                    print(
                        f"Parsing failed after {max_retries} attempts due to ConnectionResetError."
                    )
                    raise

    def update_forecast_properties(self):
        """
        Updates forecast properties based on the latest parsed data.
        """
        self.valid_times = self.data.data.keys()
        earliest_step = min(self.valid_times)
        self.data_levels = self.data.data[earliest_step].keys()
        self.coordinates = np.dstack((self.data.latitudes, self.data.longitudes))
        self.coordinates = np.dstack((self.data.latitudes, self.data.longitudes))

    def get_data(self):
        """
        Gets all the forecast data from the grid.

        Returns:
            dict: A dictionary containing all the forecast data.
        """
        data = {}
        for date_time in self.valid_times:
            local_time = utc_to_finnish(date_time)
            time_str = local_time.strftime("%Y-%m-%d %H:%M:%S")
            coordinates_data = {}
            for level in self.data_levels:
                datasets = self.data.data[date_time][level]
                for dataset_name, dataset in datasets.items():
                    unit = dataset["units"]
                    data_array = dataset["data"]
                    for (lat_index, lon_index), data_value in np.ndenumerate(
                        data_array
                    ):
                        latitude = self.coordinates[lat_index, lon_index, 0]
                        longitude = self.coordinates[lat_index, lon_index, 1]
                        key = str((latitude, longitude))
                        if key not in coordinates_data:
                            coordinates_data[key] = []
                        coordinates_data[key].append(
                            {"Dataset": dataset_name, "Unit": unit, "Data": data_value}
                        )
            data[time_str] = coordinates_data
        return data

    def get_coordinates(self):
        """
        Returns all available coordinates within the bounding box area.

        Returns:
            list: List of coordinate pairs.
        """
        unique_coords = set()

        flattened_coords = [
            tuple(coord) for sublist in self.coordinates for coord in sublist
        ]

        for coord in flattened_coords:
            unique_coords.add(coord)

        return list(unique_coords)

    def get_closest_poi_coordinates_data(self, pois, aqi_data, aqi_coords):
        """
        Finds the nearest coordinates forecast data for all of the POI's coordinates.

        Args:
            pois (list): List of POI objects.

        Returns:
            dict: A dictionary containing the nearest coordinates forecast data for each hour.
        """
        data = self.get_data()
        coordinates = self.get_coordinates()
        closest_coordinates_fore = self.calculate_shortest_weather(pois, coordinates)
        closest_coodinates_aqi = self.calculate_shortest_aqi(pois, aqi_coords)

        returned_data = {hour: {} for hour in data}

        for hour, hour_data in data.items():
            for poi_coord, nearest in closest_coordinates_fore.items():
                nearest_str = f"({nearest[0]}, {nearest[1]})"
                if nearest_str in hour_data:
                    forecast = hour_data[nearest_str]
                    returned_data[hour][
                        f"{poi_coord[0]}, {poi_coord[1]}"
                    ] = self.parse_forecast(forecast)

        for datetime, coordinates_list in closest_coodinates_aqi.items():
            if datetime not in aqi_data:
                continue
            for poi_coord in coordinates_list:
                nearest_str = (poi_coord['nearest'][0], poi_coord['nearest'][1])
                if nearest_str in aqi_data[datetime]:
                    aqi_value = aqi_data[datetime][nearest_str][0]['Air Quality Index']
                    poi_location = f"{poi_coord['poi_coordinate'][0]}, {poi_coord['poi_coordinate'][1]}"
                    returned_data[datetime][poi_location]['Air quality'] = f'{aqi_value} AQI'

        return returned_data

    def parse_forecast(self, forecast):
        """
        Parses the desired data from the forecast grid.

        Args:
            forecast (list): List of forecast data.

        Returns:
            dict: A dictionary containing the parsed forecast data.
        """
        for value in forecast:
            if value["Dataset"] == "2 metre temperature":
                temperature = round(value["Data"] - 273.15, 1)
            elif value["Dataset"] == "2 metre relative humidity":
                humidity = round(value["Data"], 1)
            elif value["Dataset"] == "10 metre U wind component":
                u_wind = value["Data"]
            elif value["Dataset"] == "10 metre V wind component":
                v_wind = value["Data"]
            elif value["Dataset"] == "surface precipitation amount, rain, convective":
                precipitation = round(value["Data"], 1)
            elif value["Dataset"] == "Total Cloud Cover":
                cloudcoverage = round(value["Data"], 1)

        wind_speed = self.calculate_wind_speed_and_direction(u_wind, v_wind)
        return {
            "Air temperature": f"{str(temperature)} °C",
            "Humidity": f"{str(humidity)} %",
            "Wind speed": f"{wind_speed} m/s",
            "Precipitation": f"{precipitation} mm",
            "Cloud amount": f"{cloudcoverage} %",
        }

    def calculate_wind_speed_and_direction(self, u_wind, v_wind):
        """
        Calculates the wind speed and direction based on the U and V components.

        Args:
            u_wind (float): U component of the wind.
            v_wind (float): V component of the wind.

        Returns:
            tuple: A tuple containing the wind speed and direction.
        """
        wind_speed = math.sqrt(u_wind**2 + v_wind**2)
        wind_direction = math.atan2(u_wind, v_wind) * (180 / math.pi)
        wind_direction = (wind_direction + 360) % 360
        return round(wind_speed, 1)

    def calculate_shortest_weather(self, pois, fore_coordinates):
        """Calculates the nearest weather forecast data for a given poi

        Args:
            pois (list): List of POI objects.
            fore_coordinates (list): List of weather forecast coordinates as tuples

        Returns:
            list: a list containing pois and their nearest forecast weather coordinate
        """
        closest_coordinates = {}
        for poi in pois:
            smallest = float("inf")
            nearest = []
            lat = poi.latitude
            lon = poi.longitude
            for coordinate in fore_coordinates:
                dist = abs(coordinate[0] - lat) + abs(coordinate[1] - lon)
                if dist < smallest:
                    smallest = dist
                    nearest = [coordinate[0], coordinate[1]]
            closest_coordinates[(lat, lon)] = nearest
        return closest_coordinates

    def calculate_shortest_aqi(self, pois, aqi_coordinates):
        """Calculates the nearest aqi forecast data for a given poi

        Args:
            pois (list): List of POI objects.
            aqi_coordinates (dict): hour-coordinate_list dictionary of aqi data

        Returns:
            dict: nearest coordinates for given poi by hour
        """
        closest_coordinates = {}

        for poi in pois:
            lat_poi, lon_poi = poi.latitude, poi.longitude
            smallest_distances = {time: float("inf") for time in aqi_coordinates}
            nearest_coordinates = {time: None for time in aqi_coordinates}

            for time, coords_list in aqi_coordinates.items():
                for lat, lon in coords_list:
                    dist = abs(lat - lat_poi) + abs(lon - lon_poi)
                    if dist < smallest_distances[time]:
                        smallest_distances[time] = dist
                        nearest_coordinates[time] = (lat, lon)

            for time in aqi_coordinates:
                if time not in closest_coordinates:
                    closest_coordinates[time] = []

                nearest = nearest_coordinates[time]
                closest_coordinates[time].append({'poi_coordinate': [lat_poi, lon_poi], 'nearest': [nearest[0], nearest[1]]})

        return closest_coordinates
