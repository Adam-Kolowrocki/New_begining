def factorial(x):
    if x == 1:
        return x
    else:
        return x * factorial(x - 1)


user_num = int(input(f'Type integer number to calculate factorial -> '))
print(factorial(user_num))
