def function(f, number):
    return f(number)


print(function(lambda x: x * x, 3))


def square(x):
    return x * x


print(square(5))

res = (lambda x: x * x)(5)

print(res)


print(f'second = {res}')

lam1 = lambda x: x * x
print(lam1(5))
print(lam1(6))
print(lam1(7))
print(lam1(8))
print(lam1(9))
lam2 = lambda x, y, z: (x + y) * z
print(lam2(2, 3, 10))

print((lambda x, y, z: (x + y) * z)(2, 3, 6))
