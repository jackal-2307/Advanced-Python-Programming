def classify_pm25(value):
    """Classify a PM2.5 reading using the exercise's air-quality ranges.

    Parameters
    ----------
    value : int | float
        The PM2.5 value to classify.

    Returns
    -------
    str
        "Good" below 12, "Moderate" from 12 through 35, or "High" above 35.

    Raises
    ------
    TypeError
        If value is not an integer or floating-point number.
    """
    if not isinstance(value, (int, float)) or isinstance(value, bool):
        raise TypeError("value must be a number")
    if value < 12:
        return "Good"
    if value <= 35:
        return "Moderate"
    return "High"


if __name__ == "__main__":
    readings = [11.9, 12, 35, 35.1]
    results = [classify_pm25(value) for value in readings]
    assert results == ["Good", "Moderate", "Moderate", "High"]
    try:
        classify_pm25("12")
    except TypeError:
        pass
    else:
        raise AssertionError("a non-numeric reading must raise TypeError")
    print(list(zip(readings, results)))