import time


def process_time(func):
    def wrapper():
        start = time.time()
        func()
        elapsed_time = time.time() - start
        print(f"Process time: {elapsed_time}")
    return wrapper


# decorator
@process_time
def test_func():
    total = 1
    for i in range(1, 1000):
        total *= i
    print(total)


test_func()
