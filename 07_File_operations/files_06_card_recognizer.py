# Card recognizing. Make a file containing credit cards numbers. Check type of each card.
# Separate cards to different files by type, e.g. visa.txt, mastercard.txt, americanexpress.txt.

def main():
    print(f'This program recognize a credit card by number (given in file cards_numbers.txt)')


def get_card_numbers():
    """Get card numbers from file"""
    numbers_list = []
    with open('/home/adam/Dokumenty/Python-Kurs/New_beginning/07_File_operations/cards_numbers.txt', 'r') as file:
        numbers = file.readlines()
        for i in range(len(numbers)):
            numbers_list += numbers[i].split(' ')
    print(numbers_list)
    print(len(numbers_list))
    return numbers_list


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


def result_write(vi, ma, am, un):
    """Take numbers of cards and write it to the files"""
    print(f'From given numbers I have recognized cards and write result to files: visa.txt, mastercard.txt, '
          f'americanexpress.txt and unknown.txt')
    with open('visa.txt', 'w') as file:
        for i in range(len(vi)):
            file.write(vi[i] + '\n')
    with open('mastercard.txt', 'w') as file:
        for i in range(len(ma)):
            file.write(ma[i] + '\n')
    with open('americanexpress.txt', 'w') as file:
        for i in range(len(am)):
            file.write(ma[i] + '\n')
    with open('unknown.txt', 'w') as file:
        for i in range(len(un)):
            file.write(un[i] + '\n')


if __name__ == '__main__':
    main()
    result_write(*card_rec(get_card_numbers()))
