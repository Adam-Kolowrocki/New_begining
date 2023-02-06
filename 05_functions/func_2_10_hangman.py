#  Write a game "Hangman".
# Computer draws a word from list of words, prints masked word with number of letters eg. ‘- - - - - - -‘
# User give a letter. Check if letter in word, if so, print info:
# "HIT" and print letter in wright order.
# In other case print:
# "MISS" Try again.
# You can limit the number of attempts to 10.
from random import choice


def words_generator():
    """Function returns secret and hidden words"""
    words_list = ['panaceum', 'bokobrody', 'bananowy', 'magnetyczny', 'poprawkowy', 'przywileje', 'sewastopol',
                  'pokemony', 'naturalizacja', 'mistyfikacja', 'polowanie', 'maskarada', 'książka', 'posiadłość']
    secret_word = choice(words_list)
    hidden_word = '_' * len(secret_word)
    temp_word = secret_word
    print(f'This is a funny game "HANGMAN" \n')
    print(f'User have to guess hidden word chosen from list.\n')
    return secret_word, hidden_word, temp_word


def main_body(secret_word, hidden_word, temp_word):
    """Function find letter given by user in a secret word and return info."""
    trial_counter = 0
    while trial_counter < 10:
        user_input = input(f'Type a letter You want to check or whole word if You know it -> ')
        if user_input == secret_word:
            print(f'Congratulation!!!\nYou have guess the hidden word!')
            print(f'It really was  " {secret_word} " ')
            break
        elif user_input in secret_word:
            while user_input in temp_word:
                replace_index = temp_word.find(user_input)
                hidden_word = hidden_word[:replace_index] + user_input + hidden_word[replace_index + 1:]
                temp_word = temp_word[:replace_index] + 'X' + temp_word[replace_index + 1:]
            print(f'HIT')
            if hidden_word == secret_word:
                print(f'Congratulation!!!\nYou have guess the hidden word!')
                print(f'The secret word was  " {secret_word} " ')
                break
            print(f'Hidden word is now -> {hidden_word}')

        else:
            trial_counter += 1
            print(f'MISS...\nTry again')
    if trial_counter == 10:
        print(f'You were hanged!!!\n\nSorry....\n\nBetter luck next time.')


main_body(*words_generator())
