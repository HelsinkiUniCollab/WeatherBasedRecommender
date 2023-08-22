import math

class IndoorScorer():
    PRECIPITATION_WEIGHT = 0.7
    TEMPERATURE_WEIGHT = 0.1
    CLOUDS_WEIGHT = 0.04
    WIND_SPEED_WEIGHT = 0.03
    DAY_TIME_WEIGHT = 0.06
    HUMIDITY_WEIGHT = 0.02
    OPTIMAL_TEMPERATURE_LOW = 20
    OPTIMAL_TEMPERATURE_HIGH = 25
    HUMIDITY_LOW = 0.4
    HUMIDITY_HIGH = 0.55
    AIR_QUALITY_WEIGHT = 0.05

    @staticmethod
    def temperature_score(temperature):
        if IndoorScorer.OPTIMAL_TEMPERATURE_LOW <= temperature <= IndoorScorer.OPTIMAL_TEMPERATURE_HIGH:
            return 0
        elif temperature < IndoorScorer.OPTIMAL_TEMPERATURE_LOW:
            return 1 - math.exp(-0.04 * (IndoorScorer.OPTIMAL_TEMPERATURE_LOW - temperature))
        else:
            return 1 - math.exp(0.2 * (IndoorScorer.OPTIMAL_TEMPERATURE_HIGH - temperature))
        
    @staticmethod
    def day_time_score(current_time, sunrise_time, sunset_time):
        if sunrise_time <= current_time <= sunset_time:
            return IndoorScorer.DAY_TIME_WEIGHT
        return 0

    @staticmethod
    def humidity_score(humidity):
        if humidity < IndoorScorer.HUMIDITY_LOW or humidity > IndoorScorer.HUMIDITY_HIGH:
            return IndoorScorer.HUMIDITY_WEIGHT
        return 0

    def score(self, temperature, wind_speed, humidity, precipitation, clouds, air_quality, sunrise_time, sunset_time, current_time):
        score = (IndoorScorer.PRECIPITATION_WEIGHT * (1 - math.exp(-10 * precipitation)) +
                 IndoorScorer.TEMPERATURE_WEIGHT * self.temperature_score(temperature) +
                 self.day_time_score(current_time, sunrise_time, sunset_time) +
                 IndoorScorer.CLOUDS_WEIGHT * (1 - math.exp(-3 * clouds)) +
                 IndoorScorer.WIND_SPEED_WEIGHT * (1 - math.exp(-0.3 * wind_speed)) +
                 self.humidity_score(humidity) +
                 IndoorScorer.AIR_QUALITY_WEIGHT * math.exp(0.5 * (1 - air_quality)))
        return round(score, 2)
