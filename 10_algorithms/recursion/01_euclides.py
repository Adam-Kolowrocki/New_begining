# Find the highest common divisor of two natural numbers. Use Euclides algorithm.
print(f'Returns highest common divisor of 2 naturals given by user.')
num_1 = int(input(f'Type the first number -> '))
num_2 = int(input(f'Type the second number ->  '))


def euclides(a, b):
    if a % b == 0:
        return b
    else:
        c = a % b
        a, b = b, c
        return euclides(a, b)


print(f'The highest common divisor of {num_1} and {num_2} is {euclides(num_1, num_2)}')
