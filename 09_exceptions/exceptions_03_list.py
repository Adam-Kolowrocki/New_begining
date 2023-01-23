# Create a list of 10 elements of a different types. Let User give an index.
# Divide 1 by number on given index. Handle the errors.

my_list = [43, '66', 'typhon', 459, 99, 'morale', 234, 745, 'a3', 'ggg', 56382, 3492, 0]
user_idx = int(input(f'Type an index in range from 0 to {len(my_list) - 1} -> '))

try:
    print(1 / my_list[user_idx])
except TypeError:
    print(f'You can not divide by non integer element of the list...')
except ZeroDivisionError:
    print(f'You can not divide by "0"...')

