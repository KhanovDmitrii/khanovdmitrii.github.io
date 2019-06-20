import datetime


def wrap(func):
    def time(*args, **kwargs):
        start = datetime.datetime.now()
        res = func(*args)
        print(datetime.datetime.now() - start)
        return res
    return time

@wrap
def func(a, b, c):
    return a*b*c

print(func(10000, 100, 9))
