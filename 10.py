import time

def timer(val1):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = val1(*args, **kwargs)
        end = time.time()
        print(f"Function {val1.__name__} took {end-start:.4f} seconds")
        return result
    return wrapper

@timer
def heavy_computation(n):
    return sum(i * i for i in range(n))

numbers = range(1, 6)
squared = list(map(lambda x: x * x, numbers))
filtered = list(filter(lambda x: x > 10, squared)