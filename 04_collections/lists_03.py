# On the given by User list of integer numbers, check if the first one is equal to last one.
number_count = int(input(f'How many numbers do You want to add to list -> '))
numbers_list = []
for number in range(0, number_count):
    number = int(input(f'Type an integer number -> '))
    numbers_list.append(number)
if numbers_list[0] == numbers_list[-1]:
    print(f'The first and the last given number are equal.')
else:
    print(f'The first and the last given number are NOT equal.')
