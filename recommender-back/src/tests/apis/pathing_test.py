import unittest
from src.apis.pathing import GreenPathsAPI

class TestGreenPathsAPI(unittest.TestCase):
    def test_fetch_api_data(self):
        start_coords = (60.172808, 24.909591)
        end_coords = (60.204516, 24.962033)
        green_paths = GreenPathsAPI(start_coords, end_coords)
        api_response = green_paths.api_response
        self.assertIsInstance(api_response, dict)

        expected_keys = ["path_FC", "edge_FC"]
        for key in expected_keys:
            self.assertIn(key, api_response)

        expected_types = {
            "path_FC": dict,
            "edge_FC": dict,
        }

        for key, expected_type in expected_types.items():
            self.assertIsInstance(api_response[key], expected_type)

    def test_extract_path_coordinates(self):
        start_coords = (60.172808, 24.909591)
        end_coords = (60.204516, 24.962033)
        green_paths = GreenPathsAPI(start_coords, end_coords)
        route_coordinates = green_paths.route_coordinates

        self.assertIsInstance(route_coordinates, list)
        self.assertTrue(route_coordinates, "No route coordinates available.")

        for coord in route_coordinates:
            self.assertIsInstance(coord, list)
            self.assertEqual(len(coord), 2)

        for latitude, longitude in route_coordinates:
            self.assertIsInstance(latitude, (int, float))
            self.assertIsInstance(longitude, (int, float))
            self.assertGreaterEqual(latitude, -90.0)
            self.assertLessEqual(latitude, 90.0)
            self.assertGreaterEqual(longitude, -180.0)
            self.assertLessEqual(longitude, 180.0)

if __name__ == '__main__':
    unittest.main()