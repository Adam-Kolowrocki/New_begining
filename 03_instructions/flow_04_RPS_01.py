# Write a game - rock (r) / paper (p) / scissors (s).
#   User gives one of 3 options.
#   Computer gives random option.
#   Check, who won the round.   -   version 01
#   Change the code, give user option to chose count of rounds.
#   The result is given by a numbers of sum of won rounds computer vs user.
#   Change the code, give user option to end the game anytime, for example typing "end".
from random import choice
print(f'Lets play a game - Rock/Paper/Scissors')
print(f'\nYou cant typ one of "r" as for rock, "p" as for paper or "s" as for scissors.')
user_choice = input(f'\nWhat is Your choice -> ')
options = 'r', 'p', 's'
comp_choice = choice(options)
if user_choice == comp_choice:
    print(f'You chose "{user_choice}" and computer choose "{comp_choice}" as well.')
    print(f'It was a draw')
elif comp_choice == "r" and user_choice == "p":
    print(f'You chose "{user_choice}" and computer choose "{comp_choice}".')
    print(f'You have won.')
elif comp_choice == "r" and user_choice == "s":
    print(f'You chose "{user_choice}" and computer choose "{comp_choice}".')
    print(f'The computer won.')
elif comp_choice == "p" and user_choice == "r":
    print(f'You chose "{user_choice}" and computer choose "{comp_choice}".')
    print(f'The computer won.')
elif comp_choice == "p" and user_choice == "s":
    print(f'You chose "{user_choice}" and computer choose "{comp_choice}".')
    print(f'You have won.')
elif comp_choice == "s" and user_choice == "p":
    print(f'You chose "{user_choice}" and computer choose "{comp_choice}".')
    print(f'The computer won.')
elif comp_choice == "s" and user_choice == "r":
    print(f'You chose "{user_choice}" and computer choose "{comp_choice}".')
    print(f'You have won.')
