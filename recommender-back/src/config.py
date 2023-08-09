class Config:
    BBOX = '24.5,60,25.5,60.5'
    TIMESTEP = 60
    FORECAST_PARAMETERS = 'Temperature,Humidity,WindUMS,WindVMS,PrecipitationAmount,TotalCloudCover'
    AIRQUALITY_PARAMETERS = 'AQINDEX_PT1H_avg'
    CACHE_REDIS_URL = 'redis://redis:6379/0'
