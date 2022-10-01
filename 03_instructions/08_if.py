# Sorting.
# Tree variable numbers given by User save as variables.
# Find the greatest one. Print in order from smallest to largest.
print('This is a small sorting code.')
print('Type tree numbers and I try to sort them...')
print()
number_1 = input('Type the first one -> ')
number_2 = input('Type the second -> ')
number_3 = input('Type the third -> ')
if number_1 > number_2 > number_3:
    print(f'The first number "{number_1}" is the largest one.')
    print(f'Sorted numbers are: {number_3}, {number_2}, {number_1}')
elif number_1 > number_3 > number_2:
    print(f'The first number "{number_1}" is the largest one.')
    print(f'Sorted numbers are: {number_2}, {number_3}, {number_1}')
elif number_2 > number_1 > number_3:
    print(f'The second number "{number_2}" is the largest one.')
    print(f'Sorted numbers are: {number_3}, {number_1}, {number_2}')
elif number_2 > number_3 > number_1:
    print(f'The second number "{number_2}" is the largest one.')
    print(f'Sorted numbers are: {number_1}, {number_3}, {number_2}')
elif number_3 > number_1 > number_2:
    print(f'The third number "{number_3}" is the largest one.')
    print(f'Sorted numbers are: {number_2}, {number_1}, {number_3}')
else:
    print(f'The third number "{number_3}" is the largest one.')
    print(f'Sorted numbers are: {number_1}, {number_2}, {number_3}')
