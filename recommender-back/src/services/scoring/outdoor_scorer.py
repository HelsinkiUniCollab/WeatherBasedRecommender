import math

class OutdoorScorer:
    PRECIPITATION_WEIGHT = 0.35
    TEMPERATURE_WEIGHT = 0.3
    CLOUDS_WEIGHT = 0.04
    WIND_SPEED_WEIGHT = 0.04
    DAY_TIME_WEIGHT = 0.2
    HUMIDITY_WEIGHT = 0.02
    OPTIMAL_TEMPERATURE_LOW = 20
    OPTIMAL_TEMPERATURE_HIGH = 25
    HUMIDITY_LOW = 0.4
    HUMIDITY_HIGH = 0.55
    AIR_QUALITY_WEIGHT = 0.05

    @staticmethod
    def temperature_score(temperature):
        if OutdoorScorer.OPTIMAL_TEMPERATURE_LOW <= temperature <= OutdoorScorer.OPTIMAL_TEMPERATURE_HIGH:
            return 1
        elif temperature < OutdoorScorer.OPTIMAL_TEMPERATURE_LOW:
            return math.exp(-0.1 * (OutdoorScorer.OPTIMAL_TEMPERATURE_LOW - temperature))
        else:
            return math.exp(0.1 * (OutdoorScorer.OPTIMAL_TEMPERATURE_HIGH - temperature))

    @staticmethod
    def day_time_score(current_time, sunrise_time, sunset_time):
        if sunrise_time <= current_time <= sunset_time:
            return OutdoorScorer.DAY_TIME_WEIGHT
        return 0

    @staticmethod
    def humidity_score(humidity):
        if OutdoorScorer.HUMIDITY_LOW <= humidity <= OutdoorScorer.HUMIDITY_HIGH:
            return OutdoorScorer.HUMIDITY_WEIGHT
        return 0

    def score(self, temperature, wind_speed, humidity, precipitation, clouds, air_quality, sunrise_time, sunset_time, current_time):
        score = (OutdoorScorer.PRECIPITATION_WEIGHT * math.exp(-precipitation) +
                 OutdoorScorer.TEMPERATURE_WEIGHT * self.temperature_score(temperature) +
                 self.day_time_score(current_time, sunrise_time, sunset_time) +
                 OutdoorScorer.CLOUDS_WEIGHT * math.exp(-clouds) +
                 OutdoorScorer.WIND_SPEED_WEIGHT * math.exp(-wind_speed) +
                 self.humidity_score(humidity) + 
                 OutdoorScorer.AIR_QUALITY_WEIGHT * math.exp(1 - air_quality))
        return round(score, 2)
