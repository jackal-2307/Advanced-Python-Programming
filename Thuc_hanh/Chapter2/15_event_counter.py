def create_counter():
    """Return a closure that increments and reports its running count.

    Calling the closure without an argument adds one; passing an amount adds
    that amount. Each closure keeps an independent count, initially zero.

    Returns
    -------
    callable
        A counter accepting an optional increment amount.
    """
    count = 0

    def counter(amount=1):
        nonlocal count
        count += amount
        return count

    return counter


if __name__ == "__main__":
    counter = create_counter()
    assert [counter(), counter(3), counter()] == [1, 4, 5]
    print(1)
    print(4)
    print(5)