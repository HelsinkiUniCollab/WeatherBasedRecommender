import unittest
from ..app import app


class AppTestCase(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    def test_index_route(self):
        response = self.client.get('/')
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], 'Hello from the backend!')
        self.assertEqual(data['status'], 200)

    def test_not_found_error_handler(self):
        response = self.client.get('/nonexistent')
        error_data = response.get_json()
        self.assertEqual(response.status_code, 404)
        self.assertEqual(error_data['message'], 'Resource not found')
        self.assertEqual(error_data['status'], 404)


if __name__ == '__main__':
    unittest.main()
