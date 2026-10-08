def run_pipeline(values, functions):
    """Apply each function to every value, in the order given.

    A new list is created at each step, leaving the input list unchanged.
    The transformed list is printed after every function and returned at the end.

    Parameters
    ----------
    values : list
        The initial values.
    functions : list[callable]
        Functions applied in sequence to each value.

    Returns
    -------
    list
        The values after all transformations.
    """
    result = list(values)
    for function in functions:
        result = [function(value) for value in result]
        print(result)
    return result


if __name__ == "__main__":
    values = [3, 6, 9]
    functions = [lambda value: value * 2, lambda value: value + 1, lambda value: round(value / 3, 2)]
    assert run_pipeline(values, functions) == [2.33, 4.33, 6.33]
    assert values == [3, 6, 9]
    assert run_pipeline([1, 2, 3], [lambda value: value * 2, lambda value: value + 1]) == [3, 5, 7]