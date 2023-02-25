# Text analysis
def main():
    print(f'I will return some information about text...')
    if menu() == "s":
        result, text = open_file("inwokacja.txt", "a")
        print(f'The letter You were looking appears {result} times in text.')
        other_stats(text)
    else:
        result, text = open_file(*user_input())
        print(f'The letter You were looking appears {result} times in text.')
        other_stats(text)


def menu():
    print(f'You can give your file name as text source and letter to be count, or use standard variables.')
    user_opt = ("s", "u")
    user_decision = ""
    while user_decision not in user_opt:
        print(f'Type "s" for standard or "u" for User data')
        user_decision = input(f'What is Your choice -> ').lower()
    return user_decision


def user_input():
    user_file = input(f'Type name of txt file with text to analysis -> ')
    user_letter = input(f'Type a letter to find and count in text -> ')
    return user_file, user_letter


def open_file(filename, par):
    with open(filename, "r") as file:
        text = file.read()
    return counter(text.lower(), par), text


def other_stats(text):
    for z in "aąbcćdeęfghijklłmnoóprsśtuwxyzźż":
        count = counter(text.lower(), z)
        print('{0} - {1} - {2}%'.format(z.upper(), count, round(count/len(text) * 100)))


def counter(txt, x):
    count = 0
    for a in txt:
        if a == x:
            count += 1
    return count


if __name__ == "__main__":
    main()
