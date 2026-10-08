from functools import wraps
from time import perf_counter


def timer(func):
    """Print a function's execution time and return its result."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        elapsed = perf_counter() - start
        print(f"[TIMER] Function: {func.__name__}; elapsed: {elapsed:.6f} seconds")
        return result

    return wrapper


@timer
def sum_of_squares(n):
    return sum(value**2 for value in range(n))


if __name__ == "__main__":
    assert sum_of_squares(100_000) == sum(value**2 for value in range(100_000))
    assert sum_of_squares(1_000_000) == sum(value**2 for value in range(1_000_000))