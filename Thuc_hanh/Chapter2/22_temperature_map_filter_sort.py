temperatures = [28, 31, 35, 29, 37, 33]
fahrenheit = list(map(lambda celsius: celsius * 9 / 5 + 32, temperatures))
hot_days_celsius = list(filter(lambda celsius: celsius > 32, temperatures))
hot_days_descending = sorted(hot_days_celsius, reverse=True)

if __name__ == "__main__":
    assert fahrenheit == [82.4, 87.8, 95.0, 84.2, 98.6, 91.4]
    assert hot_days_descending == [37, 35, 33]
    print(fahrenheit)
    print(hot_days_descending)