from random import choice
file_name = input(f'Type a file to import quotes -> ')
if '/' not in file_name:
    file_name = '/home/adam/Dokumenty/Python-Kurs/Files/' + file_name
else:
    file_name = file_name
with open(file_name, 'r') as quotas:
    day_quota = choice(quotas.readlines())
    day_quota = day_quota.split('||')
    print(f'\nQuote of the day is:\n'.center(140))
    print('*' * 140 + '\n')
    print(day_quota[0].center(140) + '\n')
    print(day_quota[1].center(140))
    print('*' * 140 + '\n')
