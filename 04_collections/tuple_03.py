# Create a tuple of integers. Ask user to type random number.
# If user number in tuple, return index.
numbers_tuple = (3, 6, 9, 2, 4, 6, 8, 9, 0, 7, 6, 3, 4, 7, 8, 1, 3, 4, 6, 8, 0)
user_number = int(input(f'Type an integer number to find in the tuple -> '))
if user_number in numbers_tuple:
    index = numbers_tuple.index(user_number)
    print(f'Your number is in tuple on index {index}.')
else:
    print(f'Your number is not in tuple.')
