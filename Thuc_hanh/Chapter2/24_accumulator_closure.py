def create_accumulator():
    """Return a closure that adds each supplied value to a running total."""
    total = 0

    def accumulate(value):
        nonlocal total
        total += value
        return total

    return accumulate


if __name__ == "__main__":
    accumulator = create_accumulator()
    results = [accumulator(10), accumulator(5), accumulator(20)]
    assert results == [10, 15, 35]
    print(*results, sep="\n")