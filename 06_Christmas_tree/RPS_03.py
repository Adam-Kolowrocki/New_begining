# Add option to continue the game regardless of the number of rounds selected.
# After each round ask user if he wants to continue "Would you like to continue yes/no:"
# if no, ask again
# "No!? We had so much fun together! You will not get away so easily!
# Prepare yourself for the next round!"
# And start a round. Add menu with options and welcome screen.
# Welcome:                      Level selection:
# S - Start                     Difficulty level:
# P - Difficulty level          A - Smart
# Q - Quit                      B - Stupid
#
# Standardize communicates given to user:
# Your choice:
# R - Rock
# P - Paper
# S - Scissors
#
# End of game:
# Would you like to continue yes/no:
#
# You don't know how to extend difficulty level ?
# Lizard and Spock
# Like in  Big Bang Theory
# Add statistics :
# Till user break the game, collect statistics and at the end print:
# Count and percent od User wins
# The Longest sequence of user and computer wins
# Others - version 04
from random import choice


def menu():
    """Menu and info function"""
    print(f'Lets play a game - Rock/Paper/Scissors')
    print(f'\nYou can chose how many rounds You want to play...')
    user_number = int(input('Type a number of rounds -> '))
    print(f'\nAnytime You want, You can end the game just by typing "end".')
    return user_number


def main_game(user_number):
    """Function compare user choose with computer choose"""
    round_counter = 0
    draw_count = 0
    user_wins = 0
    comp_wins = 0
    while round_counter <= user_number - 1:
        options = 'r', 'p', 's'
        print(f'\nYou can chose one of "r" as for rock, "p" as for paper or "s" as for scissors.')
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
    return user_wins, comp_wins, draw_count


def game_end(user_wins, comp_wins, draw_count):
    """This function prints result and info """
    print(f'\nThere was {user_wins} round won by You, {comp_wins} rounds won by computer and {draw_count} draws.')
    if user_wins == comp_wins:
        print(f'\nSo there was a draw in a whole game.')
    elif user_wins > comp_wins:
        print(f'\nSo You won the whole game.\n\nCongratulations!!!')
    elif user_wins < comp_wins:
        print(f'\nSo the computer won whole game.\n\nSorry!!!')


game_end(*main_game(menu()))

if __name__ == "__main__":
    main()
