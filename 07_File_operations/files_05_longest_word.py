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
    words_dict = {}
    for i in range(len(words_list)):
        words_dict[i] = len(words_list[i])
    max_val = max(dict.values(words_dict))
    while True:
        j = 0
        if len(words_list[j]) < max_val:
            words_list.pop(j)
        else:
            break
    print(f'The longest word in file "inwokacja.txt" is {words_list[j]} and it is {max_val} characters long.')


if __name__ == '__main__':
    main()
