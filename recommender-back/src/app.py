import datetime
from flask import Flask
from flask_apscheduler import APScheduler
from flask_caching import Cache
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()

cache_config = {
    "DEBUG": True,
    "CACHE_TYPE": "SimpleCache",
    "CACHE_DEFAULT_TIMEOUT": 300,
}

app = Flask(__name__)
CORS(app)

cache = Cache(config=cache_config)
cache.init_app(app)


class SchedulerConfig(object):
    SCHEDULER_API_ENABLED = True
    JOBS = []


app.config.from_object(SchedulerConfig())

scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()

scheduler.add_job(
    id="current_weather_job",
    func="src.services.tasks:get_current_weather_data",
    trigger="interval",
    minutes=20,
    next_run_time=datetime.datetime.now() + datetime.timedelta(seconds=10),
)

scheduler.add_job(
    id="forecast_job",
    func="src.services.tasks:update_forecast_data",
    trigger="interval",
    minutes=30,
    next_run_time=datetime.datetime.now(),
)

from src import routes