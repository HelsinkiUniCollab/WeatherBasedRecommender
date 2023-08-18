import cachetools

qtime_cache = cachetools.TTLCache(maxsize=1, ttl=86400)

def set_cache(key, value):
  qtime_cache[key] = value

def get_cache(key):
  return qtime_cache.get(key)
