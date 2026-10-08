stations = [
    {"id": "A01", "name": "Tan Son Hoa", "pm25": 32.5, "temp": 30.1},
    {"id": "A02", "name": "Thu Duc", "pm25": 18.2, "temp": 29.4},
    {"id": "A03", "name": "Bien Hoa", "pm25": 41.8, "temp": 31.0},
    {"id": "A04", "name": "Nha Be", "pm25": 32.5, "temp": 28.8},
]

sorted_stations = sorted(stations, key=lambda station: (-station["pm25"], station["temp"]))
station_names = list(map(lambda station: station["name"], sorted_stations))

if __name__ == "__main__":
    assert station_names == ["Bien Hoa", "Nha Be", "Tan Son Hoa", "Thu Duc"]
    print(station_names)