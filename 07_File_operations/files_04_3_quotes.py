from random import choice
import os
file_name = input(f'Type a file to import quotes -> ')
if file_name == '':
    file_name = 'quotes.txt'
if '/' not in file_name:
    file_name = '/home/adam/Dokumenty/Python-Kurs/Files/' + file_name
else:
    file_name = file_name
number = 0
print(f'\n 3 random quotes for today are:\n'.center(140))
print('*' * 140 + '\n')
while number < 3:
    with open(file_name, 'r') as quotas:
        day_quota = choice(quotas.readlines())
        day_quota = day_quota.split('||')
        print(day_quota[0].center(140))
        print(day_quota[1].center(140))
        number += 1
print('*' * 140 + '\n')
print(f'The file You point is {os.path.getsize(file_name)} bytes long.')
