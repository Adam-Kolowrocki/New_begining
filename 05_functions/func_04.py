# Write a function which returns every even elements from given list of elements (use function from task 2)
def if_even(u_list):
    """This function check if numbers given in list are even."""
    result_list = []
    for elem in u_list:
        if elem % 2 == 0:
            result_list.append(elem)
    return result_list


user_list = []
print(f'This code returns even elements of list given by user.\n')
elem_count = int(input(f'Hov many elements do You want to add to list -> '))
for n in range(1, elem_count + 1):
    user_ele = int(input(f'Type {n} number -> '))
    user_list.append(user_ele)

print(if_even(user_list))
