def classify_values(values, classifier):
    """Return a mapping from each value to the label produced by classifier.

    Parameters
    ----------
    values : iterable
        Values to classify.
    classifier : callable
        A function that accepts one value and returns its label.

    Returns
    -------
    dict
        Each input value mapped to its classification label.
    """
    return {value: classifier(value) for value in values}


def classify_temperature(temp):
    if temp < 20:
        return "cool"
    if temp <= 32:
        return "normal"
    return "hot"


def classify_pm25(value):
    if value < 12:
        return "Good"
    if value <= 35:
        return "Moderate"
    return "High"


if __name__ == "__main__":
    assert classify_values([18, 25, 35], classify_temperature) == {
        18: "cool", 25: "normal", 35: "hot"
    }
    assert classify_values([11.9, 12, 35, 35.1], classify_pm25) == {
        11.9: "Good", 12: "Moderate", 35: "Moderate", 35.1: "High"
    }
    print(classify_values([18, 25, 35], classify_temperature))
    print(classify_values([11.9, 12, 35, 35.1], classify_pm25))