# Write a function for factorial with iteration (eg. for loop) and with recursion.
import time

print(f'Calculate factorial of N given by User in two ways.')
numb = int(input(f'Type a number to calculate factorial -> '))


def factorial_iter(s):
    fac_iter = 1
    for i in range(1, s + 1):
        fac_iter = fac_iter * i
    return fac_iter


def factorial_rec(s):
    if s == 1:
        return s
    else:
        return s * factorial_rec(s - 1)


st_for = time.time()
print(f'Factorial of {numb} with "for" loop is -> {factorial_iter(numb)} ')
et_for = time.time()
print(f'It lasted {(et_for - st_for) * 1000} ms ')
st_rec = time.time()
print(f'Factorial of {numb} with recursion -> {factorial_rec(numb)} ')
et_rec = time.time()
print(f'It lasted {(et_rec - st_rec) * 1000} ms ')
