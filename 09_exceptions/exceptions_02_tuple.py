# Create a Tuple with s few values - e.g. 10. Let user type random index and value.
# Try to replace value of given index in tuple.  Handle the error.

my_tuple = (12, 34, 56, 90, 45, 87, 32, 65, 43, 100, 111)
user_val = input(f'Type a value You want to add to Tuple -> ')
user_idx = int(input(f'Type an index on which You want to place it in range from 0 to {len(my_tuple) - 1} -> '))

try:
    my_tuple[user_idx] = user_val
except TypeError:
    print(f"You can't modify Tuple!!!")
