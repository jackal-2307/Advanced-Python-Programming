from functools import wraps


def log_step(func):
    """Log the step name and input/output list sizes."""
    @wraps(func)
    def wrapper(values, *args, **kwargs):
        before_count = len(values)
        result = func(values, *args, **kwargs)
        print(
            f"[STEP] {func.__name__}: "
            f"{before_count} elements before, {len(result)} after"
        )
        return result

    return wrapper


@log_step
def remove_non_numeric(values):
    """Return only integer and floating-point values from the input list."""
    return list(filter(lambda value: isinstance(value, (int, float)), values))


@log_step
def remove_negative(values):
    """Return only non-negative values from the input list."""
    return list(filter(lambda value: value >= 0, values))


@log_step
def clip_upper_bound(values, upper=500):
    """Cap every value at upper, returning a new list."""
    return [min(value, upper) for value in values]


@log_step
def round_values(values, digits=1):
    """Round every value to the requested number of decimal digits."""
    return list(map(lambda value: round(value, digits), values))


def run_pipeline(values, functions):
    """Apply each list transformation in order and return its result and stats.

    The input list is copied before any function is applied.
    """
    result = list(values)
    for function in functions:
        result = function(result)

    statistics = {
        "count": len(result),
        "sum": sum(result),
        "mean": sum(result) / len(result) if result else None,
        "min": min(result) if result else None,
        "max": max(result) if result else None,
    }
    return result, statistics


if __name__ == "__main__":
    raw_pm25 = [12.5, -999, None, 18.0, "NA", 35.2, -1, 42.6, 20.1]
    cleaned, statistics = run_pipeline(
        raw_pm25,
        [remove_non_numeric, remove_negative, clip_upper_bound, round_values],
    )
    assert cleaned == [12.5, 18.0, 35.2, 42.6, 20.1]
    assert raw_pm25 == [12.5, -999, None, 18.0, "NA", 35.2, -1, 42.6, 20.1]
    assert statistics == {"count": 5, "sum": 128.4, "mean": 25.68, "min": 12.5, "max": 42.6}
    print(cleaned)
    print(statistics)