# Take an even number of elements for the list. check if 2 middle elements are equal.
element_count = -1
while element_count % 2 != 0:
    element_count = int(input(f'How many elements do You want to add to list (it has to be even number) -> '))
elements_list = []
for element in range(0, element_count):
    element = input(f'Type an element -> ')
    elements_list.append(element)
middle = int(len(elements_list)/2)
if elements_list[middle - 1] == elements_list[middle]:
    print(f'The two middle elements are equal.')
else:
    print(f'The two middle elements are NOT equal.')
