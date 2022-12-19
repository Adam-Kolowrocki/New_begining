# Learn more about ASCII coding. Make a scrypt creating simple coded message, each letter save as ASCII number.
# Get familiar with ord() and chr() methods. Remember to add separator.
# Write second script, which decrypt Your massage.
def main():
    """Main function of the script."""
    print(f'Welcome')
    print(f'This is a short massage encrypter.')
    input(f'Press enter to continue...')
    menu()


def menu():
    """This function gives option to save coded massage into a specific file"""
    user_decision = []
    user_options = ['y', 'n']
    while user_decision not in user_options:
        user_decision = input(f'Do You want to save Your massage into specific or standard file? [Y/N]-> ').lower()
    if user_decision == 'y':
        user_filename = input(f'Type the name of Your file -> ')
    else:
        massage_output(input_massage(), 'coded')
        return
    return massage_output(input_massage(), user_filename)


def input_massage():
    """Take a massage from User to be encoded and encode it."""
    massage = input(f'Type Your massage to be encoded ->')
    coded_massage = []
    for i in range(len(massage)):
        coded_massage.append(ord(massage[i]))
    coded_string = ''
    for i in range(len(coded_massage)):
        coded_string += str(coded_massage[i]) + ","
    return coded_string


def massage_output(coded_string, filename):
    """Save coded massage to the txt file."""
    with open(f'./{filename}.txt', '+w') as file:
        file.write(str(coded_string))
    print(f'The massage was encrypted and saved in a file named {filename}.txt')


if __name__ == '__main__':
    main()
