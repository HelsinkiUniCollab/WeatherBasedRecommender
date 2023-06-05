class PointOfInterest:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.contract_type = kwargs.get('contract_type')
        self.name = kwargs.get('name')
        self.street_address = kwargs.get('street_address')
        self.municipality = kwargs.get('municipality')
        self.service_nodes = kwargs.get('service_nodes')
        self.location = kwargs.get('location')
        self.geometry = kwargs.get('geometry')
        self.accessibility_shortcoming_count = kwargs.get('accessibility_shortcoming_count')
        self.object_type = kwargs.get('object_type')
        self.weather = kwargs.get('weather')

    def calculate_score(self):
        temperature_str = self.weather['Air temperature']
        humidity_str = self.weather['Humidity']

        temperature = float(temperature_str.split()[0])
        humidity = float(humidity_str.split()[0])

        # Calculate the score based on humidity and temperature
        # You can define your own scoring logic here

        if humidity is None or temperature is None:
            return -float('inf')

        suitable_temperature_range = (25, 35)
        suitable_humidity_range = (40, 60)

        if suitable_temperature_range[0] <= temperature <= suitable_temperature_range[1]:
            temperature_score = 1.0
        else:
            temperature_score = 0.0

        if suitable_humidity_range[0] <= humidity <= suitable_humidity_range[1]:
            humidity_score = 1.0
        else:
            humidity_score = 0.0

        score = (temperature_score + humidity_score) / 2
        return score


