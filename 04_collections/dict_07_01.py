# Remove duplicates from given list and create a tuple from it. Find min amd max value in tuple.
#  example_list = [34, 17, 25, 41, 12, 194, 41, 3, 12, 99, 94]

example_list = [34, 17, 25, 41, 12, 194, 41, 3, 12, 99, 94]
new_list = []
for i in range(len(example_list)):
    if example_list[i] not in new_list:
        new_list.append(example_list[i])
new_tuple = tuple(new_list)
print(new_tuple)
min_val = min(new_tuple)
max_val = max(new_tuple)
print(f'The min value in tuple is {min_val} and the max is {max_val}.')
