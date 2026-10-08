def make_power(power):
    """Return a function that raises its input to the captured power."""
    def calculate(value):
        return value**power

    return calculate


if __name__ == "__main__":
    square = make_power(2)
    cube = make_power(3)
    assert square(4) == 16
    assert cube(4) == 64
    print(square(4))
    print(cube(4))