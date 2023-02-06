n = int(input(f'Type natural number to find sum of numbers from 1 to Your number -> '))


def sum_for(n):
    s = 0
    for i in range(1, n + 1):
        s = s + i
    return s


print(f'Sum (with "for" loop) of natural number from 1 to {n} is {sum_for(n)}')


def sum_while(n):
    s = 0
    while n > 0:
        s += n
        n -= 1
    return s


print(f'Sum (with "while" loop) of natural number from 1 to {n} is {sum_while(n)}')


def sum_rec(n):
    if n == 1:
        return n
    else:
        return n + sum_for(n - 1)


print(f'Sum (with recursion) of natural number from 1 to {n} is {sum_rec(n)}')
