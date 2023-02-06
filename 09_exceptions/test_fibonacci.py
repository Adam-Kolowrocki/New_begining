def fibonacci(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fibonacci(x - 1) + fibonacci(x - 2)


user_num = int(input(f'Type integer number to calculate fibonacci string -> '))
print(fibonacci(user_num))
