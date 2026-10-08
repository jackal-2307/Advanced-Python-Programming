def square(n):
    """Return the square of an integer or floating-point number.

    Parameters
    ----------
    n : int | float
        The number to square.

    Returns
    -------
    int | float
        n multiplied by itself.
    """
    return n**2


def is_even(n):
    """Check whether an integer is even.

    Parameters
    ----------
    n : int
        The integer to check.

    Returns
    -------
    bool
        True if n is divisible by two, otherwise False.
    """
    return n % 2 == 0


def celsius_to_fahrenheit(c):
    """Convert a temperature in degrees Celsius to Fahrenheit.

    Parameters
    ----------
    c : int | float
        A temperature in degrees Celsius.

    Returns
    -------
    float
        The temperature in degrees Fahrenheit.
    """
    return c * 9 / 5 + 32


if __name__ == "__main__":
    assert square(4) == 16
    assert is_even(8) is True
    assert is_even(7) is False
    assert celsius_to_fahrenheit(25) == 77.0
    print(square(4), is_even(8), celsius_to_fahrenheit(25))