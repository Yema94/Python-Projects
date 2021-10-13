from functools import wraps
import logging

def debug(func):
    log = logging.getLogger(func.__module__)
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(log.debug(func.__qualname__))
        print(func.__qualname__)
        return func(*args, **kwargs)
    return wrapper