def make_threshold_checker(threshold, inclusive=True):
    """Create a function that checks values against a captured threshold.

    Parameters
    ----------
    threshold : int | float
        The comparison threshold.
    inclusive : bool, default=True
        Use >= when true and > when false.

    Returns
    -------
    callable
        A checker accepting one value.
    """
    if inclusive:
        return lambda value: value >= threshold
    return lambda value: value > threshold


if __name__ == "__main__":
    is_high = make_threshold_checker(35)
    assert is_high(30) is False
    assert is_high(40) is True
    assert make_threshold_checker(35, inclusive=False)(35) is False
    print(is_high(30))
    print(is_high(40))