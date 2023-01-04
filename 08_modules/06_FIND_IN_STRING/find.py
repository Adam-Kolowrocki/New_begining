#  Stwórz program, który dla dowolnego ciągu znajduje najdłuższą sekwencję takich samych znaków oraz jej długość np.
# Wejście:       var = ‘banannnnannnnnnnnnanananananaaaana’
# Wyjście :      ‘nnnnnnnnn’, 9
import test_gen
input_str = 'banannnnannnnnnnnnanananananaaaana'


def main():
    print(f'This program finds longest sequent of the same sign in a given string... ')
    user_options = ['u', 'c', 's']
    user_choice = ''
    while user_choice not in user_options:
        user_choice = input(f'If You want to give Your set of characters to generate string, press "u",\n'
                            f'if You want computer to generate string from characters 0 to 9, press "c",\n'
                            f'if You want to use standard string, press "s" -> ').lower()
    if user_choice == "s":
        find_longest(list_of_sequences(input_str))
    elif user_choice == "c":
        find_longest(list_of_sequences(test_gen.num_gen()))
    elif user_choice == "u":
        user_set = test_gen.user_set()
        find_longest(list_of_sequences(test_gen.user_gen(user_set)))


def string_input():
    user_str = input(f'Type a string to analyze and find longest sequence -> ')
    return user_str


def find_sequence(string, i):
    sequence = ''
    while i < len(string) - 1:
        if string[i] == string[i + 1]:
            sequence += string[i]
            i += 1
            continue
        elif string[i] == string[i - 1]:
            sequence += string[i]
            return sequence, i
        else:
            i += 1
    return sequence, i


def list_of_sequences(string):
    i = 0
    sequences_list = []
    while i < len(string) - 1:
        rep_seq, pos = find_sequence(string, i)
        sequences_list.append(rep_seq)
        i = pos + 1
    return sequences_list


def find_longest(sequences):
    longest = max(sequences, key=len)
    print(f'The longest repeated sequence is {longest} and it is {len(longest)} characters long.')


if __name__ == "__main__":
    main()
