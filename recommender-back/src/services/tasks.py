from ..app import celery
from ..apis.forecast import Forecast

@celery.task(bind=True)
def fetch_data(self, weather_fetcher):
    forecast = Forecast(weather_fetcher)
    forecast.update_data()
