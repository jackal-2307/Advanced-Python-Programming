def summarize(values):
    """Return the count, sum, mean, minimum, and maximum of numeric values.

    Parameters
    ----------
    values : list[int | float]
        A non-empty list of numbers to summarize.

    Returns
    -------
    dict[str, int | float]
        Summary values under the keys count, sum, mean, min, and max.

    Raises
    ------
    ValueError
        If values is empty.
    """
    if not values:
        raise ValueError("values must not be empty")

    return {
        "count": len(values),
        "sum": sum(values),
        "mean": sum(values) / len(values),
        "min": min(values),
        "max": max(values),
    }


if __name__ == "__main__":
    integer_summary = summarize([1, 2, 3, 4])
    float_summary = summarize([1.5, 2.5, 4.0])
    assert integer_summary == {"count": 4, "sum": 10, "mean": 2.5, "min": 1, "max": 4}
    assert float_summary == {"count": 3, "sum": 8.0, "mean": 8.0 / 3, "min": 1.5, "max": 4.0}
    try:
        summarize([])
    except ValueError:
        pass
    else:
        raise AssertionError("summarize([]) must raise ValueError")
    print(integer_summary)
    print(float_summary)