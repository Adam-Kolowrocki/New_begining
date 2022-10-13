# Without using min() function write Your own one which finds the lowest value from 3 numbers.
# minimum_of(a, b, c).
def minimum_of(a, b, c):
    if a < b and a < c:
        print(f'The lowest value is -> {a}.')
    elif b < a and b < c:
        print(f'The lowest value is -> {b}.')
    else:
        print(f'The lowest value is -> {c}.')


print(f'This code returns the lowest value from 3 given.')
a = int(input(f'Type first integer number to compare -> '))
b = int(input(f'Type second integer number to compare -> '))
c = int(input(f'Type third integer number to compare -> '))
minimum_of(a, b, c)
