# FLAMES is a game which name is an acronym of Friends, Lovers, Affectionate, Marriage, Enemies, Sibling.
# It can be used as a prophecy.
# Take names of two persons. Remove letters which ar in both names. Count letters You have left.
# Use the number of letters and word "FLAMES" to find relationship...

def main():
    """The main function"""
    print(f'This is a short game checking relationship between two people...\n')
    print(f'You give me Your names, I give You result...\n')
    input(f'Press any kay to continue...')
    name_collect()


def name_collect():
    """The function collects input data and delete letters which are in both of them"""
    person_1 = input(f'Type name of first person ->').lower()
    person_2 = input(f'Type name of second person ->').lower()
    for letter in person_1:
        if letter in person_2:
            person_1 = person_1.replace(letter, '')
            person_2 = person_2.replace(letter, '')
    check_string = person_1 + person_2
    relationship_test(len(check_string))


def relationship_test(x):
    """This function find relationship type"""
    flames = 'FLAMES'
    while x > len(flames):
        x -= len(flames)
    proph = flames[x - 1]
    prophecy(proph)


def prophecy(x):
    """This function returns prophecy"""
    if x == 'F':
        print(f'You will be Friends for ever...')
    elif x == 'L':
        print(f'You will be a Lovers.')
    elif x == 'A':
        print(f'There is Affectionate between You...')
    elif x == 'M':
        print(f'Soon You will get Marriage...')
    elif x == 'E':
        print(f'Sorry, You will become en Enemies.')
    elif x == 'S':
        print(f"Didn't You known that You are Siblings ???")
    else:
        print(f'There has to be some kind of mistake...')


if __name__ == "__main__":
    main()
