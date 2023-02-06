# Remove duplicates from given list and create a tuple from it. Find min amd max value in tuple.
#  example_list = [34, 17, 25, 41, 12, 194, 41, 3, 12, 99, 94]

example_list = [34, 17, 25, 41, 12, 194, 41, 3, 12, 99, 94]
set_tmp = set(example_list)
example_tuple = tuple(set_tmp)
print(example_tuple)
min_val = min(example_tuple)
max_val = max(example_tuple)
print(f'The min value in tuple is {min_val} and the max is {max_val}.')
