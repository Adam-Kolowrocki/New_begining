import os

filename = 'inwokacja.txt'
if os.path.isfile(filename):
    with open(filename, 'r') as file:
        print(file.read())
else:
    print(f'Thera is no such file...')
