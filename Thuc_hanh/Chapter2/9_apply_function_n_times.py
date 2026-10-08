def apply_n_times(func, value, n):
    """Apply func to value repeatedly, exactly n times.

    Parameters
    ----------
    func : callable
        A function accepting the current value and returning its replacement.
    value : object
        The initial value.
    n : int
        A non-negative number of applications.

    Returns
    -------
    object
        The value after n applications, or the initial value when n is zero.

    Raises
    ------
    ValueError
        If n is negative.
    """
    if n < 0:
        raise ValueError("n must not be negative")
    for _ in range(n):
        value = func(value)
    return value


if __name__ == "__main__":
    assert apply_n_times(lambda value: value + 2, 1, 4) == 9
    assert apply_n_times(lambda value: value + 1, 5, 3) == 8
    assert apply_n_times(lambda value: value**2, 2, 2) == 16
    assert apply_n_times(lambda value: value + 1, 5, 0) == 5
    try:
        apply_n_times(lambda value: value, 1, -1)
    except ValueError:
        pass
    else:
        raise AssertionError("negative n must raise ValueError")
    print(apply_n_times(lambda value: value + 2, 1, 4))