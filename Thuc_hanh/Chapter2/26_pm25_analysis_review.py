from functools import wraps


pm25_values = [12.5, 18.2, 35.1, 28.4, 41.8, 20.6, 30.2]


def log_call(func):
    """Log the name of the function whenever it is called."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] Function: {func.__name__}")
        return func(*args, **kwargs)

    return wrapper


@log_call
def calculate_mean(values):
    """Return the arithmetic mean of a non-empty list of PM2.5 values.

    Parameters
    ----------
    values : list[int | float]
        PM2.5 measurements.

    Returns
    -------
    float
        The arithmetic mean.

    Raises
    ------
    ValueError
        If values is empty.
    """
    if not values:
        raise ValueError("values must not be empty")
    return sum(values) / len(values)


def make_threshold_checker(threshold):
    """Return a closure checking whether a value is greater than threshold."""
    return lambda value: value > threshold


def transform_values(values, func):
    """Apply func to each value and return a new list."""
    return [func(value) for value in values]


if __name__ == "__main__":
    above_25 = list(filter(lambda value: value > 25, pm25_values))
    is_high = make_threshold_checker(35)
    normalized = transform_values(pm25_values, lambda value: value / max(pm25_values))
    assert above_25 == [35.1, 28.4, 41.8, 30.2]
    assert [value for value in pm25_values if is_high(value)] == [35.1, 41.8]
    assert max(normalized) == 1.0
    assert calculate_mean(pm25_values) == sum(pm25_values) / len(pm25_values)
    print(above_25)
    print(normalized)