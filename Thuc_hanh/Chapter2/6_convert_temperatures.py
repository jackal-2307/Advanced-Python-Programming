temperatures_c = [20, 25, 30, 35, 40]
temperatures_f = list(map(lambda celsius: round(celsius * 9 / 5 + 32, 1), temperatures_c))
labels = list(map(lambda celsius: "hot" if celsius > 32 else "normal", temperatures_c))

if __name__ == "__main__":
    assert temperatures_f == [68.0, 77.0, 86.0, 95.0, 104.0]
    assert labels == ["normal", "normal", "normal", "hot", "hot"]
    print(temperatures_f)
    print(labels)