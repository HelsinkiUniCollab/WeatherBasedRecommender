import numpy as np
import tempfile
import pytz
import requests
import defusedxml.ElementTree as ET
from urllib.parse import urlencode
from netCDF4 import Dataset
from ..config import Config
from datetime import datetime, timedelta
from fmiopendata.grid import download_and_parse
from .times import get_forecast_times

class AQI:
    def __init__(self):
        """A class representing a single AQI object

        Args:
            data (numpy array): aqi data as numpy array
            json (string): full parsed aqi data in json format
            dataset (netcdf): netcdf dataset containing the aqi data
            datetimes (dict): dictionary containing datetimes and aqi objects
            latitudes (numpy array): latitude coordinates as numpy array
            longitudes (numpy array): longitude coordinates as numpy array
        """
        self.data = None
        self.json = None
        self.dataset = None
        self.datetimes = None
        self.latitudes = None
        self.longitudes = None

    def download_netcdf_and_store(self):
        """Downloads netcdf file, parses it and stores the data in the object.
           The temporary file is deleted afterwards.
        """
        netcdf_file_url = self._get_and_parse_xml()

        with tempfile.NamedTemporaryFile(delete=True) as temp_file:
            netcdf_file_name = temp_file.name
            print('Downloading AQI data')
            self._download_to_file(netcdf_file_url, netcdf_file_name, 5)
            print('Finished downloading AQI data. Parsing the data...')
            self.dataset = Dataset(netcdf_file_name)
            self._parse_netcdf()

    def _get_and_parse_xml(self):
        """Downloads and parses xml file based on the given query

        Returns:
            string: url link of latest queried netcdf file
        """
        _, start_time, end_time = get_forecast_times()
        args = {'starttime': start_time, 'endtime': end_time, 'parameters': Config.AQI_PARAMS, 'bbox': Config.BBOX}

        url = Config.FMI_QUERY_URL + Config.AQI_QUERY + "&" + urlencode(args)
        req = requests.get(url)
        content = req.content
        xml = ET.fromstring(content)
        file_reference = xml.findall(Config.FILEREF_MEMBER)

        latest_file_url = file_reference[-1].text

        return latest_file_url
    
    def _parse_netcdf(self):
        """Parses the given netcdf file

        Returns:
            dict: A dictionary of datetimes keys and AQI object values
        """
        self.latitudes = self.dataset.variables['lat'][:]
        self.longitudes = self.dataset.variables['lon'][:]
        time = self.dataset.variables['time'][:-1]
        aqi = self.dataset.variables['index_of_airquality_194'][:]

        finland_tz = pytz.timezone('Europe/Helsinki')
        server_time = datetime.now()
        converted = server_time.astimezone(finland_tz)
        forecast_time = converted + timedelta(hours=1)

        datetimes = {}
        for times in time:
            forecast_datetime = forecast_time + timedelta(hours=int(times))
            forecast_datetime = forecast_datetime.replace(minute=0, second=0, microsecond=0)
            aqi_data = aqi[int(times)]
            aqi_obj = AQI()
            aqi_obj.data = aqi_data
            datetimes[forecast_datetime] = aqi_obj

        self.datetimes = datetimes
        self.dataset.close()

    def to_json(self):
        """Converts the parsed netcdf data into JSON format. Any zero aqi values are skipped
           so that the final coordinates will never contain any zeros.

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
                aqi_value = aqi_object.data[lat_index, lon_index]

                if aqi_value != 0:
                    if coord_pairs not in coordinate_data:
                        coordinate_data[coord_pairs] = []
                        coordinate_data[coord_pairs].append({'Air Quality Index': 
                                                             str(aqi_value)})

            data[time_str] = coordinate_data

        self.json = data

        return data

    def get_coordinates(self):
        """Fetches all coordinates by their respective hours

        Returns:
            dict: hourly coordinates in form of key: hour value: coord_list
        """
        unique_coords = {}
        for hour, hour_data in self.json.items():
            coords_list = []
            for coord_tuple in hour_data.keys():
                lat, lon = coord_tuple
                coords_list.append((float(lat), float(lon)))
            unique_coords[hour] = coords_list
        return unique_coords

    def _download_to_file(self, url, file_name, max_retries):
        """Downloads the file content

        Args:
            url (string): url of the file to be downloaded
            file_name (string): name of the file
            max_retries (int): maximum number of retries
        """
        for retry_attempt in range(max_retries-1):
             try:
                with open(file_name, 'wb') as file:
                    response = requests.get(url, stream=True)
                    for chunk in response.iter_content(chunk_size=8192):
                        file.write(chunk)
                    return
             except (requests.RequestException, ConnectionResetError) as e:
                print(f"Download attempt {retry_attempt + 1} failed with error: {str(e)}")
                if retry_attempt < max_retries:
                    print(f'Retrying...')
                else:
                    print(f"Maximum retries reached. Download failed.")
