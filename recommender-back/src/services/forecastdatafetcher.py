from fmiopendata.wfs import download_stored_query

class ForecastDataFetcher:
    def get_forecast_data(self, start, end, bbox, timestep, parameters):
        forecast_data = download_stored_query('fmi::forecast::harmonie::surface::grid',
                                                args=[f'starttime={start}',
                                                        f'endtime={end}',
                                                        f'bbox={bbox}',
                                                        f'timestep={timestep}',
                                                        f'parameters={parameters}']
                                                        )
        return forecast_data

    def get_current_weather_data(self, bbox, timeseries):
        current_weather_data = download_stored_query('fmi::observations::weather::multipointcoverage',
                                                     args=[f'bbox={bbox}',
                                                           f'timeseries={timeseries}',]
                                                           )
        return current_weather_data
