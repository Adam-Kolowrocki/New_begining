# Write a function which take a list o numbers and returns sum of all its elements.
def list_sum(n_list):
    """This function returns a sum of elements in the given list."""
    result_sum = 0
    for elem in n_list:
        result_sum += elem
    return result_sum


user_list = []
print(f'This code returns sum of elements in list given by user.\n')
elem_count = int(input(f'Hov many elements do You want to add to list -> '))
for n in range(1, elem_count + 1):
    user_ele = int(input(f'Type {n} number -> '))
    user_list.append(user_ele)

print(list_sum(user_list))
