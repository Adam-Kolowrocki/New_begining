# Without using min() function write Your own one which finds the lowest value from 3 numbers.
# minimum_of(a, b, c).
def minimum_of(a, b, c):
    """Return maximum value from 3 given by user"""
    if a < b and a < c:
        print(f'The lowest value is -> {a}.')
    elif b < a and b < c:
        print(f'The lowest value is -> {b}.')
    else:
        print(f'The lowest value is -> {c}.')


def data_input():
    """Takes numbers from user"""
    print(f'This code returns the lowest value from 3 given.')
    a = int(input(f'Type first integer number to compare -> '))
    b = int(input(f'Type second integer number to compare -> '))
    c = int(input(f'Type third integer number to compare -> '))
    return a, b, c


minimum_of(*data_input())
