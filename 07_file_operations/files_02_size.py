from random import choice
import os
file_name = input(f'Type a file to import -> ')
if '/' not in file_name:
    file_name = '/home/adam/Dokumenty/Python-Kurs/Files/' + file_name
else:
    file_name = file_name
with open(file_name, 'r') as inwo:
    lines = choice(inwo.readlines())
    print(f'\nLines of file are:\n'.center(140))
    print('*' * 140 + '\n')
    print(lines.center(140) + '\n')
    print('*' * 140 + '\n')
print(f'The file You point is {os.path.getsize(file_name)} bytes long.')
