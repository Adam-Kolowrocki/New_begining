def greatings(name):
    print('Good morning!', name)
    return


print(greatings("Adam"))


def square(a):
    """This function returns square of variable given as parameter."""
    print(f'Square : ', a * a)


print(square.__doc__)
square(4)


def absolute_value(num):
    """Thi function returns the absolute value of the entered number"""
    if num >= 0:
        return num
    else:
        return -num


print(absolute_value(4))
print(absolute_value(-5))
