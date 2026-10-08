def make_unit_converter(scale, offset):
    """Create a converter applying y = x * scale + offset.

    Parameters
    ----------
    scale : int | float
        The multiplier.
    offset : int | float
        The value added after multiplication.

    Returns
    -------
    callable
        A function converting one input value.
    """
    def convert(value):
        return value * scale + offset

    return convert


if __name__ == "__main__":
    c_to_f = make_unit_converter(9 / 5, 32)
    assert c_to_f(25) == 77.0
    print(c_to_f(25))