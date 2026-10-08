def custom_filter(values, predicate):
    """Return values for which predicate returns True, without using filter().

    Parameters
    ----------
    values : iterable
        Values to check.
    predicate : callable
        A function returning True for values to keep.

    Returns
    -------
    list
        Values that satisfy predicate, preserving their input order.
    """
    result = []
    for value in values:
        if predicate(value):
            result.append(value)
    return result


if __name__ == "__main__":
    assert custom_filter(range(10), lambda value: value % 2 == 0) == [0, 2, 4, 6, 8]
    assert custom_filter([10, 26, 30], lambda value: value > 25) == [26, 30]
    assert custom_filter(["short", "longer", "lengthy"], lambda value: len(value) > 5) == [
        "longer", "lengthy"
    ]
    print(custom_filter(range(10), lambda value: value % 2 == 0))