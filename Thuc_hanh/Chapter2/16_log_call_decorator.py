from functools import wraps


def log_call(func):
    """Log a function's name, positional and keyword arguments, and result."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"[LOG] Function: {func.__name__}")
        print(f"[LOG] args: {args}")
        print(f"[LOG] kwargs: {kwargs}")
        print(f"[LOG] result: {result}")
        return result

    return wrapper


@log_call
def calculate_mean(values):
    return sum(values) / len(values)


if __name__ == "__main__":
    assert calculate_mean([10, 20, 30]) == 20.0