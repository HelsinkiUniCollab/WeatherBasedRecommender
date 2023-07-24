import numpy as np
from netCDF4 import Dataset
from datetime import datetime, timedelta
from fmiopendata.grid import download_and_parse
from times import get_forecast_times

class AQI:
    def __init__(self):
        self.grid_times = self._download_and_parse_xml()
        self.data = None
        self.url = None
        self.latitudes = None
        self.longitudes = None

    # only downloads the file url from xml right now
    def download_netcdf(self):
        latest_forecast = max(self.grid_times.data.keys())
        self.data = self.grid_times.data[latest_forecast]
        self.url = self._replace_bbox_in_url(self.data.url, '24.5,60,25.5,60.5')

    def _download_and_parse_xml(self):
        _, start, end = get_forecast_times()
        query_id = 'fmi::forecast::enfuser::airquality::helsinki-metropolitan::grid'
        params = 'AQIndex'
        args = [f'starttime={start}', f'endtime={end}', f'parameters={params}']
        return download_and_parse(query_id, args)

    def _parse_netcdf(self, nc_file_path):
        data = Dataset(nc_file_path)

        self.latitudes = data.variables['lat'][:]
        self.longitudes = data.variables['lon'][:]
        time = data.variables['time'][:]
        aqi = data.variables['index_of_airquality_194']

        datetimes = {}
        current_time = datetime.now() + timedelta(hours=1)
        for times in time:
            current_datetime = current_time + timedelta(hours=int(times))
            current_datetime = current_datetime.replace(minute=0, second=0, microsecond=0)
            aqi_index = aqi[int(times)]
            aqi_obj = AQI()
            aqi_obj.data = aqi_index
            datetimes[current_datetime] = aqi_obj

        return datetimes

    def _to_json(self, nc_file_path):
        datetimes = self._parse_netcdf(nc_file_path)

        data = {}
        for datetime in datetimes:
            time_str = datetime.strftime('%Y-%m-%d %H:%M:%S')
            aqi_object = datetimes[datetime]
            coordinate_data = {}
            for lat, lon in zip(self.latitudes, self.longitudes):
                lat_index = np.where(self.latitudes == lat)[0][0]
                lon_index = np.where(self.longitudes == lon)[0][0]
                coord_pairs = str((lat, lon))
                if coord_pairs not in coordinate_data:
                    coordinate_data[coord_pairs] = []
                coordinate_data[coord_pairs].append({'Air Quality Index': aqi_object.data[lat_index, lon_index]})
            data[time_str] = coordinate_data

        return data

    def _replace_bbox_in_url(self, url, new_bbox):
        start_index = url.find('bbox=')
        end_index = url.find('&', start_index)
        new_url = url[:start_index] + 'bbox=' + new_bbox + url[end_index:]
        return new_url

if __name__ == "__main__":
    aqi = AQI()
    aqi.download_netcdf()
    #data = aqi._to_json('your_file_path_here')
    #print(data)
