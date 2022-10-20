# Add option to continue the game regardless of the number of rounds selected.
# After each round ask user if he wants to continue "Would you like to continue yes/no:"
# if no, ask again
# "No!? We had so much fun together! You will not get away so easily! Prepare yourself for the next round!"
# And start a round. Add menu with options and welcome screen.
# Welcome:                      Level selection:        Standardize communicates given to user:
# S - Start                     Difficulty level:       Your choice:
# P - Difficulty level          A - Smart               R - Rock
# Q - Quit                      B - Stupid              P - Paper
#                                                       S - Scissors
# End of game:
# Would you like to continue yes/no:
#
# You don't know how to extend difficulty level ?
# Lizard and Spock, Like in  Big Bang Theory...
# Add statistics :
# Till user break the game, collect statistics and at the end print:
# Count and percent od User wins
# The Longest sequence of user and computer wins
# Others - version 04
from random import choice
round_counter = 0
draw_count = 0
user_wins = 0
comp_wins = 0


def main():
    menu()

    if diff == "a":
        game_a(round_number)
    elif diff == "b":
        game_b(round_number)


def menu():
    """Main menu and info function"""
    print(f'Lets play a game - Rock/Paper/Scissors\n')
    print(f'You have few options:\nS - Start\nD - Difficulty level\nQ - Quit\n')
    print(f'\nYou can end the game anytime, just by typing "q".')
    user_m_choice = ""
    menu_options = ["s", "d", "q"]
    while user_m_choice.lower() not in menu_options:
        user_m_choice = input(f'What is Your Choice -> ')
    if user_m_choice == "q":
        game_end(round_counter, user_wins, comp_wins, draw_count)
    elif user_m_choice == "s":
        diff = "a"
    elif user_m_choice == "d":
        game_difficulty()
    return diff


def game_difficulty():
    print(f'You have a choice of difficulty.\nA - Smart (3 options - regular version)\nB - Stupid(5 options - Sheldon'
          f' version)')
    diff = ""
    diff_options = ["a", "b"]
    while diff.lower() not in diff_options:
        diff = input(f'What is Your choice -> ')
    return diff.lower()


def round_to_play():
    print(f'\nYou can chose how many rounds You want to play...')
    num_of_rounds = int(input('Type a number of rounds -> '))
    return num_of_rounds


def game_a(round_number):
    """Function for normal, traditional game "Rock, Paper, Scissors"."""
    while round_counter <= num_of_rounds - 1:
        options = 'r', 'p', 's'
        print(f'\nYou can chose one of \n"r" as for rock, \n"p" as for paper or \n"s" as for scissors.')
        user_choice = input(f'\nWhat is Your choice -> ')







def game_b(round_number):
    print(f'Crazy game')


def a_game(user_number):
    """Function compare user choose with computer choose"""
    while round_counter <= user_number - 1:
        options = 'r', 'p', 's'
        print(f'\nYou can chose one of "r" as for rock, "p" as for paper or "s" as for scissors.')
        user_choice = input(f'\nWhat is Your choice -> ')
        if user_choice == 'q':
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


def game_end(round_counter, user_wins, comp_wins, draw_count):
    """This function prints statistics and finish the game """
    if round_counter == 0:
        print(f'Game Over')
    else:
        print(f'\nThere was {user_wins} round won by You, {comp_wins} rounds won by computer and {draw_count} draws.')
        if user_wins == comp_wins:
            print(f'\nSo there was a draw in a whole game.')
        elif user_wins > comp_wins:
            print(f'\nSo You won the whole game.\n\nCongratulations!!!')
        elif user_wins < comp_wins:
            print(f'\nSo the computer won whole game.\n\nSorry!!!')


if __name__ == "__main__":
    main()
