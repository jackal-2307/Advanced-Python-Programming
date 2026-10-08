from functools import wraps


def extract_field(records, field):
    """Extract one named field from each record using map and a lambda."""
    return list(map(lambda record: record[field], records))


def make_pm25_classifier(threshold):
    """Create a classifier that labels readings at or above threshold as High."""
    def classify(value):
        return "High" if value >= threshold else "Moderate"

    return classify


def log_call(func):
    """Log the call details and result of a report function."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"[LOG] Function: {func.__name__}")
        print(f"[LOG] args: {args}")
        print(f"[LOG] kwargs: {kwargs}")
        print(f"[LOG] result: {result}")
        return result

    return wrapper


@log_call
def build_report(measurements, classifier):
    """Build a PM2.5 report containing station totals, statistics, and labels.

    Parameters
    ----------
    measurements : list[dict]
        Records with station, pm25, and temp fields.
    classifier : callable
        A function mapping a PM2.5 value to a label.

    Returns
    -------
    dict
        Station count, PM2.5 mean and maximum, stations above 35, and each
        station's classification.
    """
    pm25_values = extract_field(measurements, "pm25")
    high_stations = list(
        map(
            lambda record: record["station"],
            filter(lambda record: record["pm25"] > 35, measurements),
        )
    )
    return {
        "station_count": len(measurements),
        "mean_pm25": sum(pm25_values) / len(pm25_values),
        "max_pm25": max(pm25_values),
        "stations_above_35": high_stations,
        "classifications": [
            {"station": record["station"], "label": classifier(record["pm25"])}
            for record in measurements
        ],
    }


if __name__ == "__main__":
    measurements = [
        {"station": "A01", "pm25": 12.5, "temp": 28.2},
        {"station": "A02", "pm25": 37.4, "temp": 31.0},
        {"station": "A03", "pm25": 28.6, "temp": 30.4},
        {"station": "A04", "pm25": 45.2, "temp": 32.1},
        {"station": "A05", "pm25": 18.9, "temp": 29.5},
    ]
    report = build_report(measurements, make_pm25_classifier(35))
    assert report["station_count"] == 5
    assert report["mean_pm25"] == 28.52
    assert report["max_pm25"] == 45.2
    assert report["stations_above_35"] == ["A02", "A04"]