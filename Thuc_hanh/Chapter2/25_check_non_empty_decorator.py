from functools import wraps


def check_non_empty(func):
    """Raise ValueError when the first list argument is empty."""
    @wraps(func)
    def wrapper(values, *args, **kwargs):
        if not values:
            raise ValueError("Dữ liệu đầu vào không được rỗng")
        return func(values, *args, **kwargs)

    return wrapper


@check_non_empty
def calculate_mean(values):
    return sum(values) / len(values)


@check_non_empty
def find_max(values):
    return max(values)


if __name__ == "__main__":
    assert calculate_mean([1, 2, 3]) == 2
    assert find_max([1, 3, 2]) == 3
    for function in (calculate_mean, find_max):
        try:
            function([])
        except ValueError:
            pass
        else:
            raise AssertionError(f"{function.__name__} must reject an empty list")