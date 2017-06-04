from datetime import datetime
from functools import wraps, lru_cache


def time_it(func):

    @wraps(func)
    def acc_args(*args, **kwargs):

        pre_time = datetime.now()

        retva = func(*args, **kwargs)

        nex_time = datetime.now()

        print('{} took {}'.format(func.__name__,nex_time - pre_time))
        return retva

    return acc_args

# @lru_cache()
@time_it
def fib(n):
    if n <= 1:
        return 1
    else:
        return fib(n-2) + fib(n-1)

print(fib(4))

