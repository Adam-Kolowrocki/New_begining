# Create a tuple. Find elements which are repeated and print them.
test_tuple = (3, 6, 9, 2, 4, 6, 8, 9, 0, 7, 6, 3, 4, 7, 8, 1, 3, 4, 6, 8, 0)
repeated_items = []
for n in test_tuple:
    if test_tuple.count(n) > 1:
        repeated_items.append(n)
repeated_set = set(repeated_items)
print(f'Elements repeated in the test_tuple are : {repeated_set}.')
