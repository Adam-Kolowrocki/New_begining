def division(x, y):
    assert y != 0, "Assertion, y = 0."
    if y == 0:
        raise ZeroDivisionError("Division by 0")
    print(f'Result of {x} divided by {y} is {x / y}.')


try:
    division(3, 0)
except ZeroDivisionError:
    print(f'There was a Zero division error...')
    raise
