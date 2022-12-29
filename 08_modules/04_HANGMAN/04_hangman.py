#  Zmodyfikuj swoją grę wisielec tak, aby w dowolny uzasadniony sposób wykorzystać moduł lub moduły.
import files_07_hangman


def main():
    """This is a test of making a game HANGMAN with use of modules"""
    print(f'This is a funny game "HANGMAN" \n')
    print(f'User have to guess hidden word chosen from list.\n')
    words = files_07_hangman.select_category()
    secret_word, hidden_word, temp_word = files_07_hangman.words_generator(words)
    files_07_hangman.main_body(secret_word, hidden_word, temp_word)


if __name__ == "__main__":
    main()
