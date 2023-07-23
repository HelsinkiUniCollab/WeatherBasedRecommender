from unittest import TestCase
from unittest.mock import patch
from src.services.forecastdatafetcher import ForecastDataFetcher

class TestForecastDataFetcher(TestCase):
    def setUp(self):
        self.fetcher = ForecastDataFetcher()
        self.start = 'start'
        self.end = 'end'
        self.bbox = 'bbox'
        self.timestep = 'timestep'
        self.parameters = 'parameters'
        self.timeseries = 'timeseries'

    @patch('src.services.forecastdatafetcher.download_stored_query')
    def test_get_forecast_data(self, mock_download):
        mock_download.return_value = 'mock forecast data'
        
        result = self.fetcher.get_forecast_data(self.start, self.end, self.bbox, self.timestep, self.parameters)

        mock_download.assert_called_once_with('fmi::forecast::harmonie::surface::grid',
                                              args=[f'starttime={self.start}',
                                                    f'endtime={self.end}',
                                                    f'bbox={self.bbox}',
                                                    f'timestep={self.timestep}',
                                                    f'parameters={self.parameters}'])
        self.assertEqual(result, 'mock forecast data')

    @patch('src.services.forecastdatafetcher.download_stored_query')
    def test_get_current_weather_data(self, mock_download):
        mock_download.return_value = 'mock weather data'
        
        result = self.fetcher.get_current_weather_data(self.bbox, self.timeseries)

        mock_download.assert_called_once_with('fmi::observations::weather::multipointcoverage',
                                              args=[f'bbox={self.bbox}',
                                                    f'timeseries={self.timeseries}'])
        self.assertEqual(result, 'mock weather data')