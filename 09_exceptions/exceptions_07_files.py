# Return to the first task of files operations lesson, modify it for user to type file name.
# Remember to give user a chance to correct his mistake e.g. wrong letter in file name.
from random import choice


def main():
    filename_input()


def filename_input():
    file_name = input(f'Type a file to import quotes -> ')
    if '/' not in file_name:
        file_name = '/home/adam/Dokumenty/Python-Kurs/Files/' + file_name
    else:
        file_name = file_name
    print_quota(file_name)


def print_quota(file_name):
    try:
        with open(file_name, 'r') as quotas:
            day_quota = choice(quotas.readlines())
            day_quota = day_quota.split('||')
    except FileNotFoundError:
        print(f'No such a file, try again...')
        filename_input()
    try:
        day_quota[1] != ''
    except IndexError:
        print(f'Wrong file structure, try again...')
        filename_input()
    print(f'\nQuote of the day is:\n'.center(140))
    print('*' * 140 + '\n')
    print(day_quota[0].center(140) + '\n')
    print(day_quota[1].center(140))
    print('*' * 140 + '\n')
    exit()


if __name__ == "__main__":
    main()
