#  Stwórz program, który dla dowolnego ciągu znajduje najdłuższą sekwencję takich samych znaków oraz jej długość np.
# Wejście:       var = ‘banannnnannnnnnnnnanananananaaaana’
# Wyjście :      ‘nnnnnnnnn’, 9

input_str = 'banannnnannnnnnnnnanananananaaaana'


def main():
    print(f'This program finds longest sequent of the same sign in a given string... ')
    find_longest(list_of_sequences(input_str))
    # find_longest(list_of_sequences(string_input()))


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
