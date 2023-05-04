import time
from functools import wraps

def executionTimer(func):
    @wraps(func)
    def timewrapper(*args, **kwargs):
        beginTime = time.time()
        result = func(*args, **kwargs)
        completeTime = time.time()
        totalTime = completeTime - beginTime
        print("The", func.__name__, "method complete in:", totalTime)
        return result
    return timewrapper

@executionTimer
def exampleMethod(n:int):
    while n != 100000:
        n += 1

print(exampleMethod(0))
