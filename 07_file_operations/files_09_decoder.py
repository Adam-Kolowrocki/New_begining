def main():
    """Main function of decoder script"""
    print(f'This script decode the massage saved in a file...')
    menu()


def menu():
    """This function ask for file name with encoded massage"""
    user_decision = []
    user_options = ['y', 'n']
    print(f'You can type name of file with encoded massage or use standard one.')
    while user_decision not in user_options:
        user_decision = input(f'Do You want to specify file name with encoded massage? [Y/N]-> ').lower()
    if user_decision == 'y':
        user_filename = input(f'Type the name of file -> ')
    else:
        massage_output(file_import('coded'))
        return
    return massage_output(file_import(user_filename))


def file_import(filename):
    """Import coded data from a file a nd return it"""
    with open(f'./{filename}.txt', 'r') as file:
        coded_string = file.readline()
    code = []
    while len(coded_string) > 0:
        stop_coma = coded_string.find(",")
        code.append(coded_string[:stop_coma])
        coded_string = coded_string[stop_coma + 1:]
    return code


def massage_output(code):
    decoded = ''
    for i in range(len(code)):
        decoded += chr(int(code[i]))
    print(f'Decoded massage looks like this:')
    print(decoded.center(100))


if __name__ == '__main__':
    main()
