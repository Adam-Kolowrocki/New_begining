# Use file inwokacja.txt. Find the longest word in text.


def main():
    find_longest(words_list=get_words_list())


def get_words_list():
    words_list = []
    with open('/home/adam/Dokumenty/Python-Kurs/Files/inwokacja.txt', 'r') as inwokacja:
        text = inwokacja.readlines()
        for i in range(len(text)):
            words_list += text[i].split(' ')
    return words_list


def find_longest(words_list):
    for i in range(len(words_list)):
        if len(words_list[1])


if __name__ == '__main__':
    main()
