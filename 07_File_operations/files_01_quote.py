from random import choice
with open('/home/adam/Dokumenty/Python-Kurs/Files/quotas.txt', 'r') as quotas:
    day_quota = choice(quotas.readlines())
    print(f'\nQuote of the day is:\n'.center(140))
    print('*' * 140 + '\n')
    print(day_quota.center(140))
    print('*' * 140 + '\n')
