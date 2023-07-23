import netCDF4 as nc
from fmiopendata.grid import download_and_parse
from times import get_forecast_times

class AQI:
    def __init__(self):
        self.grid = self._download_and_parse_xml()
        self.data = None
        self.url = None

    def update_data(self):
        latest_forecast = max(self.grid.data.keys())
        self.data = self.grid.data[latest_forecast]
        self.url = self._replace_bbox_in_url(self.data.url, '24.5,60,25.5,60.5')
        
        print('download url:')
        print(self.url)

        #print('downloading aqi:')
        #self.data.download()
        #self.data._fname = self.nc_file
        #self._parse_netcdf(self.nc_file)

    def _download_and_parse_xml(self):
        _, start, end = get_forecast_times()
        query_id = 'fmi::forecast::enfuser::airquality::helsinki-metropolitan::grid'
        params = 'AQIndex'
        args = [f'starttime={start}', f'endtime={end}', f'parameters={params}']
        return download_and_parse(query_id, args)

    def _parse_netcdf(self, nc_file):
        data = nc.Dataset(nc_file)
        print(data)

    # for some reason bbox as args in _download_and_parse_xml was not functioning
    def _replace_bbox_in_url(self, url, new_bbox):
        start_index = url.find('bbox=')
        end_index = url.find('&', start_index)
        new_url = url[:start_index] + 'bbox=' + new_bbox + url[end_index:]
        return new_url

if __name__ == "__main__":
    aqi = AQI()
    aqi.update_data()
    #aqi._parse_netcdf()
