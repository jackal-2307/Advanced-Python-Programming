def parse_sensor_record(record):
    """Parse a comma-separated sensor record with exactly five fields.

    The input format is station_id,station_name,timestamp,pm25,temperature.
    PM2.5 and temperature are converted to floats.

    Parameters
    ----------
    record : str
        One sensor record in the specified comma-separated format.

    Returns
    -------
    dict[str, str | float]
        The parsed station ID, station name, timestamp, PM2.5, and temperature.

    Raises
    ------
    ValueError
        If the record does not contain exactly five fields or a number is invalid.
    """
    fields = record.split(",")
    if len(fields) != 5:
        raise ValueError("record must contain exactly five fields")

    station_id, station_name, timestamp, pm25, temperature = fields
    return {
        "station_id": station_id,
        "station_name": station_name,
        "timestamp": timestamp,
        "pm25": float(pm25),
        "temperature": float(temperature),
    }


if __name__ == "__main__":
    record = "TSH01,Tan Son Hoa,2026-09-09 08:00,31.5,29.2"
    expected = {
        "station_id": "TSH01",
        "station_name": "Tan Son Hoa",
        "timestamp": "2026-09-09 08:00",
        "pm25": 31.5,
        "temperature": 29.2,
    }
    assert parse_sensor_record(record) == expected
    try:
        parse_sensor_record("TSH01,Tan Son Hoa,31.5,29.2")
    except ValueError:
        pass
    else:
        raise AssertionError("a four-field record must raise ValueError")
    print(parse_sensor_record(record))