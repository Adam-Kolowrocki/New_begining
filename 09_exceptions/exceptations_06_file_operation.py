# Call error with file opening.
#  Try read file that does not exist.
#  Try read value from file open with "w".
#  Try to make file that exist in "x" mode.
#  Handle each error how You want to.
import io

try:
    with open('marabut.txt', 'r') as file_1:
        text = file_1.read()
    print(text)
except FileNotFoundError:
    print(f'The file You wanted to read those not exist.')

try:
    with open('errors.txt', 'w') as file_2:
        errors = file_2.read()
        print(errors)
except io.UnsupportedOperation:
    print(f'You cant read from file opened in "w" mode.')

try:
    with open('errors.txt', 'x') as file_3:
        test = file_3.read()
        print(test)
except FileExistsError:
    print(f'You cannot create file, it already exist.')
