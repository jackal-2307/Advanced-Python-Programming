from functools import wraps
from inspect import signature


def require_non_empty(func):
    """Reject an empty list or tuple passed as the decorated function's first argument."""
    parameters = signature(func).parameters
    first_parameter = next(iter(parameters), None)

    @wraps(func)
    def wrapper(*args, **kwargs):
        bound_arguments = signature(func).bind_partial(*args, **kwargs)
        values = bound_arguments.arguments.get(first_parameter)
        if isinstance(values, (list, tuple)) and not values:
            raise ValueError("Dữ liệu đầu vào không được rỗng")
        return func(*args, **kwargs)

    return wrapper


@require_non_empty
def calculate_mean(values):
    return sum(values) / len(values)


@require_non_empty
def calculate_max(values):
    return max(values)


@require_non_empty
def calculate_min(values):
    return min(values)


if __name__ == "__main__":
    assert calculate_mean([1, 2, 3]) == 2
    assert calculate_max((1, 3, 2)) == 3
    assert calculate_min(values=[1, 3, 2]) == 1
    for function in (calculate_mean, calculate_max, calculate_min):
        try:
            function([])
        except ValueError as error:
            assert str(error) == "Dữ liệu đầu vào không được rỗng"
        else:
            raise AssertionError(f"{function.__name__} must reject empty data")