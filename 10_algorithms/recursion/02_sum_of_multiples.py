# Write a code which returns sum of all multiples of 5 and 7 smaller than N given by user.
# eg. N = 21 -> 5+7+10+14+15+20 = 71

print(f'Returns sum of all multiples of 5 and 7 smaller than N given by User.')
a, b = 5, 7
num = int(input(f'Type our limit number -> '))


def s_o_m(n):
    c = 0
    for i in range(n):
        if i % a == 0 or i % b == 0:
            c += i
    return c


print(f'Sum of all multiples of 5 and 7 smaller than {num} is : {s_o_m(num)}')
