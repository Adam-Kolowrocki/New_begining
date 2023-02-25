#  Get familiar with Pascals triangle. Write a code to show Pascals triangle for given N.
print(f'Returns Pascals Triangle of N given by user.')
user_n = int(input(f'What is Your N -> '))
# (a+b)n


def pascals_triangle(n):
    a, b = 1, 1
    if n == 0:
        return 1
    elif n > 0:
        return pascals_triangle(n - 1)


print(pascals_triangle(user_n))
