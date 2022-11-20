# Card recognizing. Make a file containing credit cards numbers. Check type of each card.
# Separate cards to different files by type, e.g. visa.txt, mastercard.txt, americanexpress.txt.

def main():
    print(f'This program recognize a credit card by number (given in program)')


def get_card_numbers():
    """Get card numbers from file"""
    numbers_list = []
    with open('/home/adam/Dokumenty/Python-Kurs/New_beginning/07_File_operations/cadrs_numbers.txt', 'r') as inwokacja:
        text = inwokacja.readlines()
        for i in range(len(text)):
            words_list += text[i].split(' ')
    return words_list

def card_rec(card_numbers):
    """This function recognize credit cards by they number."""
    visa = []
    master = []
    american = []
    unknown = []
    for number in card_numbers:
        if (number[0: 2] == '34' or '37') and (len(number) == 15):
            american.append(number)
        elif number[0] == '4' and (len(number) == 13 or 16):
            visa.append(number)
        elif (len(number) == 16) and ((number[0: 2] == '51' or '55') or (number[0: 4] == '2221' or '2720')):
            master.append(number)
        else:
            unknown.append(number)
    return visa, master, american, unknown


def result(vi, ma, am, un):
    """Print results of card_rec"""
    print(f'From given numbers I have recognized as follows: ')
    print(f'Those are Visa numbers : {vi}.')
    print(f'Those are MasterCard numbers : {ma}.')
    print(f'Those are American Express numbers : {am}.')
    print(f'Those numbers are unknown : {un}.')


result(*card_rec(card_numbers))



if __name__ == '__main__':
    main()