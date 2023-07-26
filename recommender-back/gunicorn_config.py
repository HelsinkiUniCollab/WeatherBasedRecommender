import multiprocessing

BIND = "0.0.0.0:8000"
workers = multiprocessing.cpu_count() * 2 + 1
WORKER_CLASS = "gevent"
PRELOAD_APP = True
