import unittest
from unittest.mock import patch, Mock, call
from src.apis.aqi import AQI

class TestAQI(unittest.TestCase):
    def setUp(self):
         self.aqi = AQI()

    # latest file url is always at the bottom of the fmi xml file
    @patch('requests.get')
    def test_parse_xml_returns_latest_file_reference(self, mock_requests_get):

      mocked_xml_content = """
            <root xmlns:gml="http://www.opengis.net/gml/3.2">
                <members>
                    <gml:fileReference>older_netcdf_file_url</gml:fileReference>
                </members>
                <members>
                    <gml:fileReference>latest_netcdf_file_url</gml:fileReference>
                </members>
            </root>
      """

      mock_response = Mock()
      mock_response.content = mocked_xml_content.encode()
      mock_requests_get.return_value = mock_response
      latest_file_reference = self.aqi._parse_xml()
      expected_latest_file_reference = 'latest_netcdf_file_url'
      self.assertEqual(latest_file_reference, expected_latest_file_reference)

    @patch('requests.get')
    @patch('builtins.open', create=True)
    def test_download_to_file_successful(self, mock_open, mock_requests_get):
        mock_iterator = Mock()
        mock_iterator.iter_content.return_value = [b'chonk', b'chunky', b'chonky']
        mock_requests_get.return_value = mock_iterator

        file_name = 'some_random_file_from_fmi_that_takes_ages_to_load.nc'
        url = 'http://example.com/some_random_file_from_fmi_that_takes_ages_to_load.nc'
        max_retries = 3

        with patch('builtins.print'):
          self.aqi._download_to_file(url, file_name, max_retries)

        mock_requests_get.assert_called_once_with(url, stream=True, timeout=240)
        mock_open.assert_called_once_with(file_name, 'wb')

        mock_nc_file = mock_open.return_value.__enter__.return_value
        expected_calls = [call(b'chonk'), call(b'chunky'), call(b'chonky')]
        mock_nc_file.write.assert_has_calls(expected_calls)
