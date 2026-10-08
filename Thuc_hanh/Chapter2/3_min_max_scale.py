def min_max_scale(values):
    """Return a new list scaled to the range 0 through 1.

    The formula is (value - min(values)) / (max(values) - min(values)).
    If all values are equal, return zeros because the denominator is zero and
    every value is at the minimum.

    Parameters
    ----------
    values : list[int | float]
        Values to normalize.

    Returns
    -------
    list[float]
        A new list of normalized values. The input list is not modified.
    """
    if not values:
        return []

    minimum = min(values)
    maximum = max(values)
    if maximum == minimum:
        return [0.0 for _ in values]
    return [(value - minimum) / (maximum - minimum) for value in values]


if __name__ == "__main__":
    original = [2, 4, 6]
    assert min_max_scale(original) == [0.0, 0.5, 1.0]
    assert original == [2, 4, 6]
    assert min_max_scale([5, 5, 5]) == [0.0, 0.0, 0.0]
    assert min_max_scale([]) == []
    print(min_max_scale(original))