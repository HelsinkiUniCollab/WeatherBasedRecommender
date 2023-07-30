import requests
import matplotlib.pyplot as plt

class GreenPathsAPI:
    """
    A class for fetching route information from the Green Paths API and plotting the route on a map.

    Parameters:
        start_coords (tuple): Tuple containing the latitude and longitude of the starting point.
        end_coords (tuple): Tuple containing the latitude and longitude of the ending point.
        travel_mode (str, optional): Mode of travel, can be 'walk' or 'bike'. Defaults to 'walk'.
        routing_mode (str, optional): Routing mode, can be 'fast', 'short', 'clean', 'quiet', or 'safe' (for bikes).
            Defaults to 'fast'.
    """
    def __init__(self, start_coords, end_coords, travel_mode="walk", routing_mode="fast"):
        self.start_coords = start_coords
        self.end_coords = end_coords
        self.travel_mode = travel_mode
        self.routing_mode = routing_mode
        self.api_response = self.fetch_api_data()
        self.route_coordinates = self.extract_path_coordinates()

    def fetch_api_data(self):
        """
        Fetches route data from the Green Paths API.

        Returns:
            dict: JSON response containing route information.
        """
        url = f"https://www.greenpaths.fi/paths/{self.travel_mode}/{self.routing_mode}/{self.start_coords[0]},{self.start_coords[1]}/{self.end_coords[0]},{self.end_coords[1]}"
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()
        else:
            print("Failed to fetch data from the API.")
            return None

    def extract_path_coordinates(self):
        """
        Extracts the latitude and longitude coordinates of the route from the API response.

        Returns:
            list: List of tuples containing latitude and longitude coordinates of the route.
        """
        path_coordinates = []

        if not self.api_response:
            return path_coordinates

        path_fc = self.api_response.get("path_FC") or {}
        if not path_fc:
            return path_coordinates

        for feature in path_fc.get("features", []):
            geometry = feature.get("geometry", {})
            if geometry.get("type") == "LineString":
                path_coordinates.extend(geometry.get("coordinates", []))

        return path_coordinates

    def draw_route_line(self):
        """
        Plots the route line on a map using Matplotlib.
        Used just for verfying the path during dev
        This method displays a graph with the route line using latitude and longitude coordinates.
        """
        if not self.route_coordinates:
            print("No route coordinates available.")
            return

        longitude, latitude = zip(*self.route_coordinates)

        # Plotting 
        plt.figure(figsize=(10, 6))
        plt.title("Route Line")
        plt.xlabel("Longitude")
        plt.ylabel("Latitude")
        plt.plot(longitude, latitude, marker='o', color='blue')
        plt.show()

if __name__ == "__main__":
    # From exa to hietalahti
    start_coords = (60.172808, 24.909591)
    end_coords = (60.204516, 24.962033)
    green_paths = GreenPathsAPI(start_coords, end_coords)
    route_coordinates = green_paths.route_coordinates

    # Plotting just for testing
    #green_paths.draw_route_line()
