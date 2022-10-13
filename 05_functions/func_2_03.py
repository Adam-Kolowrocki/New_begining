# Without using max() function write Your own one which finds the highest value from 3 numbers.
# maximum_of(a, b, c).
def maximum_of(a, b, c):
    if a > b and a > c:
        print(f'The highest value is -> {a}.')
    elif b > a and b > c:
        print(f'The highest value is -> {b}.')
    else:
        print(f'The highest value is -> {c}.')


print(f'This code returns the highest value from 3 given.')
a = int(input(f'Type first integer number to compare -> '))
b = int(input(f'Type second integer number to compare -> '))
c = int(input(f'Type third integer number to compare -> '))
maximum_of(a, b, c)
