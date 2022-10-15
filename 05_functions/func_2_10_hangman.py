#  Write a game "Hangman".
# Computer draws a word from list of words, prints masked word with number of letters eg. ‘- - - - - - -‘
# User give a letter. Check if letter in word, if so, print info:
# "HIT" and print letter in wright order.
# In other case print:
# "MISS" Try again.
# You can limit the number of attempts to 10.
from random import choice
words_list = ['panaceum', 'bokobrody', 'bananowy', 'magnetyczny', 'poprawkowy', 'przywileje', 'Sewastopol',
              'pokemony', 'naturalizacja', 'mistyfikacja', 'polowanie', 'maskarada', 'książka', 'posiadłość']
secret_word = choice(words_list)
hidden_word = '_' * len(secret_word)
print(f'This is a funny game "HANGMAN" \n')
print(f'User have to guess hidden word chosen from list.')


def main_
