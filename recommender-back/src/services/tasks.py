from ..celery_worker import celery
from ..apis.forecast import Forecast
from ..services.data_fetcher import DataFetcher
from datetime import datetime

@celery.task(bind=True)
def fetch_data(self):
    try:
        print(f'Starting data fetch at {datetime.now()}...')
        weather_fetcher = DataFetcher()
        forecast = Forecast(weather_fetcher)
        forecast.update_data()
        print(f'Data fetch completed at {datetime.now()}.')
    except Exception as e:
        print(f'Data fetch failed at {datetime.now()} with error: {str(e)}.')
