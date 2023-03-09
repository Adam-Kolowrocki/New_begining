numbers = [5, 8, 11, 13, 15, 18, 20, 25, 29, 32, 35, 38, 40, 45, 48]

# Maps


def func_1(x):
    return x * 2


result = map(func_1, numbers)
print(list(result))

result_2 = map(lambda x: x * 2, numbers)
print(list(result_2))


# Filter
result_3 = filter(lambda x: x % 2 == 0, numbers)
print(list(result_3))
