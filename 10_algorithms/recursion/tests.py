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


# factorial(n)
# n! = 1*2*3*...*(n-1)*n
print('////////////////////////////////////////////////////////')
print(f'Calculate factorial of n given by User.')
n = int(input(f'What is Your n -> '))


def factorial(s):
    if s == 1:
        return s
    else:
        return s * factorial(s - 1)


print(f'Factorial from {n} = {factorial(n)}')


# fibonacci_sequence(n)
# F(n)=0+1+1+2+3+5+8+13+21+34+55+89
print('////////////////////////////////////////////////////////')
print(f'Calculate the value of given by User element of Fibonacci sequence.')
n = int(input(f'What is Your n -> '))


def fibonacci(f):
    if f == 0:
        return 0
    elif f == 1:
        return 1
    elif f == 2:
        return 1
    else:
        return fibonacci(f - 1) + fibonacci(f - 2)


print(f'The value of {n} element of Fibonacci sequence is -> {fibonacci(n)}')


def fibonacci_seq(f):
    f_seq = []
    while f > -1:
        f_seq.append(fibonacci(f))
        f -= 1
    return f_seq


fibonacci_list = fibonacci_seq(n)
fibonacci_list.reverse()
fibonacci_str = ''
for i in range(len(fibonacci_list) - 1):
    fibonacci_str += str((fibonacci_list[i])) + " + "
fibonacci_str += str(fibonacci_list[-1])
print(f'And the sequence looks like this :')
print(f'F{n} = {fibonacci_str}')
