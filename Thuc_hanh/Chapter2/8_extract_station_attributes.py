records = [
    ("A01", "Tan Son Hoa", 32.5),
    ("A02", "Thu Duc", 18.2),
    ("A03", "Bien Hoa", 41.8),
]

station_names = list(map(lambda record: record[1], records))
high_pm25_stations = list(
    map(
        lambda record: (record[1], "High"),
        filter(lambda record: record[2] > 35, records),
    )
)

if __name__ == "__main__":
    assert station_names == ["Tan Son Hoa", "Thu Duc", "Bien Hoa"]
    assert high_pm25_stations == [("Bien Hoa", "High")]
    print(station_names)
    print(high_pm25_stations)