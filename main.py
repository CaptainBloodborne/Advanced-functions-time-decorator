import functools
from typing import Dict
import time

execution_time: Dict[str, float] = {}


def time_decorator(func: callable) -> callable:
    """
    Create a decorator function `time_decorator`
    which has to calculate decorated function execution time
    and put this time value to `execution_time` dictionary where `key` is
    decorated function name and `value` is this function execution time.
    """
    start_time = time.time()

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        execution_time[func.__name__] = time.time() - start_time
        return result
    return wrapper
