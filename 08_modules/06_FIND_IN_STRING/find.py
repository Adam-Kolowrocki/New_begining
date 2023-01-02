#  Stwórz program, który dla dowolnego ciągu znajduje najdłuższą sekwencję takich samych znaków oraz jej długość np.
# Wejście:       var = ‘banannnnannnnnnnnnanananananaaaana’
# Wyjście :      ‘nnnnnnnnn’, 9

input_str = 'banannnnannnnnnnnnanananananaaaana'


def main():
    print(f'This program finds longest sequent of the same sign in a given string... ')
    find_longest(input_str)
    # find_longest(string_input())


def string_input():
    user_str = input(f'Type a string to analyze and find longest sequence -> ')
    return user_str


def find_longest(string):
    longest = ''  # 'banannnnannnnnnnnnanananananaaaana'
    sequence = ''
    i = 0
    while i < len(string) - 1:
        if string[i] == string[i + 1]:
            sequence += string[i]
            i += 1
            continue
        elif string[i] == string[i - 1]:
            sequence += string[i]
            i += 1
            continue
        else:
            i += 1

    print(sequence)
    #print(longest)


if __name__ == "__main__":
    main()
