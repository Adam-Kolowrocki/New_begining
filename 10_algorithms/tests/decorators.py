def decorator(func):
    def wrapper():
        print("--------------")
        func()
        print("--------------")
    return wrapper


def hello():
    print("Hello word")


hello = decorator(hello)
hello()


@decorator
def bye():
    print("Good By cruel word !!!")


bye()


numbers1 = {0, 1, 3, 4, 4, 6, 7, 9}
numbers2 = {1, 2, 5, 6, 7, 8, 10}
print(numbers1 | numbers2)
print(numbers1 & numbers2)
print(numbers1 - numbers2)
print(numbers1 ^ numbers2)
