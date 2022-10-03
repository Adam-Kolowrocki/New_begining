# Write a game - rock (r) / paper (p) / scissors (s).
#   User gives one of 3 options.
#   Computer gives random option.
#   Check, who won the round.
#   Change the code, give user option to chose count of rounds.
#   The result is given by a numbers of sum of won rounds computer vs user.
#   Change the code, give user option to end the game anytime, for example typing "end".    -   version 03
from random import choice
print(f'Lets play a game - Rock/Paper/Scissors')
print(f'\nYou can chose how many rounds You want to play...')
user_number = int(input('Type a number of rounds -> '))
print(f'\nAnytime You want, You can end the game just by typing "end".')
round_counter = 0
draw_count = 0
user_wins = 0
comp_wins = 0
while round_counter <= user_number - 1:
    options = 'r', 'p', 's'
    print(f'\nYou cant chose one of "r" as for rock, "p" as for paper or "s" as for scissors.')
    user_choice = input(f'\nWhat is Your choice -> ')
    if user_choice == 'end':
        break
    if user_choice not in options:
        print(f'\nYou chose wrong option.\n')
        continue
    round_counter += 1
    comp_choice = choice(options)
    if user_choice == comp_choice:
        print(f'You chose "{user_choice}" and computer choose "{comp_choice}" as well.')
        print(f'It was a draw')
        draw_count += 1
    elif comp_choice == "r" and user_choice == "p":
        print(f'You chose "{user_choice}" and computer choose "{comp_choice}".')
        print(f'You have won.')
        user_wins += 1
    elif comp_choice == "r" and user_choice == "s":
        print(f'You chose "{user_choice}" and computer choose "{comp_choice}".')
        print(f'The computer won.')
        comp_wins += 1
    elif comp_choice == "p" and user_choice == "r":
        print(f'You chose "{user_choice}" and computer choose "{comp_choice}".')
        print(f'The computer won.')
        comp_wins += 1
    elif comp_choice == "p" and user_choice == "s":
        print(f'You chose "{user_choice}" and computer choose "{comp_choice}".')
        print(f'You have won.')
        user_wins += 1
    elif comp_choice == "s" and user_choice == "p":
        print(f'You chose "{user_choice}" and computer choose "{comp_choice}".')
        print(f'The computer won.')
        comp_wins += 1
    elif comp_choice == "s" and user_choice == "r":
        print(f'You chose "{user_choice}" and computer choose "{comp_choice}".')
        print(f'You have won.')
        user_wins += 1
print(f'\nThere was {user_wins} round won by You, {comp_wins} rounds won by computer and {draw_count} draws.')
if user_wins == comp_wins:
    print(f'\nSo there was a draw in a whole game.')
elif user_wins > comp_wins:
    print(f'\nSo You won the whole game.\n\nCongratulations!!!')
elif user_wins < comp_wins:
    print(f'\nSo the computer won whole game.\n\nSorry!!!')
