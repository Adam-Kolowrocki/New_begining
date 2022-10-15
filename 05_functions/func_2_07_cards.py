# Write a program which recognize credit card by number is it Visa, MasterCard or AmericanExpress.
# What do we know about cards numbers?
# All Visa card numbers start with a 4. New cards have 16 digits. Old cards have 13.
# MasterCard numbers either start with the numbers 51 through 55 or with the numbers 2221 through 2720.
# All have 16 digits.
# American Express card numbers start with 34 or 37 and have 15 digits.
card_numbers = ('4549836495126598', '4596214635954625', '4856326185467895', '4239548762365', '4985632695148',
                '4567812365948', '5169594653152648', '5568462351468526', '2221874632654182', '2720201669541236',
                '2720564895362145', '2221486543201458', '5523694875123656', '5143697025301223', '345698462315895',
                '375694326125648', '346958963012456', '375640123056485', '374569080952614', '65684684652',
                '684489774559', '87465954223644', '7456899859465'
                )
print(f'This program recognize a credit card by number (given in program)')


def card_rec(card_numbers):
    visa = []
    master = []
    american = []
    unknown = []
    for number in card_numbers:
        if (number[0: 2] == 34 or 37) and (len(number) == 15):
            american.append(number)
        elif (number[0] == 4) and (len(number) == 13 or 16):
            visa.append(number)
        elif (len(number) == 16) and ((number[0: 2] == 51 or 55) or (number[0: 4] == 2221 or 2720)):
            master.append(number)
        else:
            unknown.append(number)
    return visa, master, american, unknown


def result(vi, ma, am, un):
    print(f'From given numbers I have recognized as follows: ')
    print(f'Those are Visa numbers : {vi}.')
    print(f'Those are MasterCard numbers : {ma}.')
    print(f'Those are American Express numbers : {am}.')
    print(f'Those numbers are unknown : {un}.')


result(*card_rec(card_numbers))
