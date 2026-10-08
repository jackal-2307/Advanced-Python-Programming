raw_values = [12.5, -999, 18.0, None, 25.4, "error", 30.2, -1]
valid_values = list(
    filter(lambda value: isinstance(value, (int, float)) and value >= 0, raw_values)
)
valid_mean = sum(valid_values) / len(valid_values) if valid_values else None

if __name__ == "__main__":
    assert valid_values == [12.5, 18.0, 25.4, 30.2]
    assert valid_mean == 21.525
    print(valid_values)
    print(valid_mean)