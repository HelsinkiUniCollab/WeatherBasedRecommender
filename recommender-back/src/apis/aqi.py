import numpy as np
import tempfile 
from netCDF4 import Dataset
from datetime import datetime, timedelta
from fmiopendata.grid import download_and_parse
from fmiopendata.utils import download_to_file
from .times import get_forecast_times

class AQI:
    def __init__(self):
        """A class representing a single AQI object

        Args:
            url (string): url link to latest netcdf aqi file
            latitudes (numpy array): latitude coordinates as numpy array
            longitudes (numpy array): longitude coordinates as numpy array
        """
        self.data = None
        self.json = None
        self.dataset = None
        self.file = None
        self.url = None
        self.datetimes = None
        self.latitudes = None
        self.longitudes = None

    def download_netcdf_and_store(self):
        """Downloads netcdf file, parses it and stores the data in the object.
           The temporary file is deleted afterwards.
        """
        grid_times = self._download_and_parse_xml()
        latest_forecast = max(grid_times.data.keys())
        self.data = grid_times.data[latest_forecast]
        self.url = self._replace_bbox_in_url(self.data.url, '24.5,60,25.5,60.5')

        if self.file is not None:
            return

        with tempfile.NamedTemporaryFile(delete=True) as temp_file:
            self.file = temp_file.name
            print('Downloading AQI data')
            download_to_file(self.url, self.file)
            print('Finished download. Parsing...')
            self.dataset = Dataset(self.file)
            self._parse_netcdf()

    def _download_and_parse_xml(self):
        """Downloads and parses xml file based on the given query
        """
        _, start, end = get_forecast_times()
        query_id = 'fmi::forecast::enfuser::airquality::helsinki-metropolitan::grid'
        params = 'AQIndex'
        args = [f'starttime={start}', f'endtime={end}', f'parameters={params}']
        return download_and_parse(query_id, args)

    def _parse_netcdf(self):
        """Parses the given netcdf file

        Returns:
            dict: A dictionary of datetimes keys and AQI object values
        """
        self.latitudes = self.dataset.variables['lat'][:]
        self.longitudes = self.dataset.variables['lon'][:]
        time = self.dataset.variables['time'][:]
        aqi = self.dataset.variables['index_of_airquality_194']

        datetimes = {}
        current_time = datetime.now() + timedelta(hours=1)
        for times in time:
            current_datetime = current_time + timedelta(hours=int(times))
            current_datetime = current_datetime.replace(minute=0, second=0, microsecond=0)
            aqi_index = aqi[int(times)]
            aqi_obj = AQI()
            aqi_obj.data = aqi_index
            datetimes[current_datetime] = aqi_obj

        self.datetimes = datetimes
        self.dataset.close()

    def _to_json(self):
        """Converts the parsed netcdf data into JSON format

        Returns:
            dict: AQI data in JSON format
        """
        data = {}
        for datetime in self.datetimes:
            time_str = datetime.strftime('%Y-%m-%d %H:%M:%S')
            aqi_object = self.datetimes[datetime]
            coordinate_data = {}
            for lat, lon in zip(self.latitudes, self.longitudes):
                lat_index = np.where(self.latitudes == lat)[0][0]
                lon_index = np.where(self.longitudes == lon)[0][0]
                coord_pairs = (lat, lon)
                if coord_pairs not in coordinate_data:
                    coordinate_data[coord_pairs] = []
                coordinate_data[coord_pairs].append({'Air Quality Index': 
                                                     str(aqi_object.data[lat_index, lon_index])})
            data[time_str] = coordinate_data

        self.json = data

        return data

    def _replace_bbox_in_url(self, url, new_bbox):
        """Takes the url and replaces the bbox coordinates with new coordinates
           This was done because the bbox arguement did not seem to work as args 

        Args:
            url (string): url of netcdf file
            new_bbox (string): new bbox values as a string i.e '24.5,60,25.5,60.5'

        Returns:
            string: new url with replaced bbox value
        """
        start_index = url.find('bbox=')
        end_index = url.find('&', start_index)
        new_url = url[:start_index] + 'bbox=' + new_bbox + url[end_index:]
        return new_url

    def get_coordinates(self):
        unique_coords = []
        for hour_data in self.json.values():
            for coord_tuple in hour_data.keys():
                lat, lon = coord_tuple
                unique_coords.append((float(lat), float(lon)))
        return unique_coords
