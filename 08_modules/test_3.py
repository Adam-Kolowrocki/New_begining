import os

filename = 'inwokacja.txt'
if os.path.isfile(filename):
    with open(filename, 'r') as f:
        print(f.read())
else:
    print('There is no such file...')
