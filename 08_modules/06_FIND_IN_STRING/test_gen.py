# Utwórz generator instancji testowych, który wygeneruje losowe ciągi znaków składające się
# z jedynie z cyfr od 0-9. Upewnij się, że conajmniej 2 takie same znaki znajdą się w sekwencji.
# Zmodyfikuj generator tak, by oczekiwał znaków podanych przez użytkownika np.
# użytkownik podaje 4 znaki: ‘a’, ‘b’, ‘c’, ‘*’.
# Zaimportuj generator bezpośrednio do programu.
import random


def main():
    """Info and Menu of script"""
    print(f'This is a random sequence generator.')
    print(f'It can generate 30 char sequence from integer numbers from 0 to 9,'
          f' or sequence of characters given by user.')
    user_choice = ''
    user_options = ['u', 'c']
    while user_choice not in user_options:
        user_choice = input(f'If You want to give Your set of characters, press "u", if not, press "c" -> ').lower()
    if user_choice == 'c':
        num_gen()
    else:
        user_gen(user_set())


def user_set():
    """Collect User set of characters"""
    user_choice_count = int(input(f'How many characters do You want to input -> '))
    user_char_list = []
    n = 1
    while user_choice_count > 0:
        user_character = input(f'Type character no {n} -> ')
        user_char_list.append(user_character)
        user_choice_count -= 1
        n += 1
    return user_char_list


def num_gen():
    """Generate random string of numbers from 0 to 9"""
    test_string = ''
    for i in range(30):
        test_string += str(random.randrange(0, 9, 1))
    return test_string


def user_gen(char_list):
    """Generate random string of characters given by user"""
    test_string = ''
    for i in range(30):
        test_string += str(random.choice(char_list))
    return test_string


if __name__ == "__main__":
    main()
