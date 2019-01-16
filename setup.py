import multiprocessing

bind = "0.0.0.0:7890"
workers = 4
errorlog = 'log/gunicorn.error.log'
accesslog = 'log/gunicorn.access.log'
loglevel = 'debug'
proc_name = 'stockoverview'
