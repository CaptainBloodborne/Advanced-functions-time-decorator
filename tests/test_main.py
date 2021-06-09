import time
from ..main import time_decorator, execution_time

TIME_100MS = 0.1


@time_decorator
def func_test1(a, b, sleep_time):
    time.sleep(sleep_time)
    return a + b


def test_f1_time_decorator():
    sleep_time = TIME_100MS
    assert 30 == func_test1(10, 20, sleep_time)
    assert execution_time[func_test1.__name__] > sleep_time
