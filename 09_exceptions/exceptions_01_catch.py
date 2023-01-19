# Create a list of few elements of different types eg. [13, ‘string’, 2.45].
# Try to divide 10 by each element of the list in the loop.
# Catch all possible Exceptions .
my_list = [4, 'gaga', 44, 'mucha', 0, 'marmelada', 3.14, 77, 0]
i = 0
while i < len(my_list):
    try:
        x = 10 / my_list[i]
        print(x)
    except TypeError:
        print(f'There was a TypeError...')
    except ZeroDivisionError:
        print(f'There was a ZeroDivisionError')
    i += 1

