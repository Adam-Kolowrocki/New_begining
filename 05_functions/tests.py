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

print('================================')
var = "global"


def my_func():
    var = "local"
    print("var inside my_func():", var)


def my_func2():
    print("var inside my_func2():", var)


my_func()
my_func2()
print("var outside:", var)

print('----------------------')
p = 'Hello!'   # p zmienna globalna


def greet(name):
    name.capitalize()  # name zmienna lokalna
    print(p, '~~~', name)


girl = 'anna'
boy = 'marc'
greet(girl)
greet(boy)

print(']]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]')


def rectangle(x, y):
    print('x * y = ' + str(x * y))
    z = 4  # zmienna z nie jest dostępna, to przypisanie NIE ZADZIAŁA


z = 3
rectangle(3, 2)
print(z)
