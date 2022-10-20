# Add menu with options and welcome screen.
# Welcome:                      Level selection:        Standardize communicates given to user:
# S - Start                     Difficulty level:       Your choice:
# P - Difficulty level          A - Smart               R - Rock
# Q - Quit                      B - Stupid              P - Paper
#                                                       S - Scissors
# End of game:
# Would you like to continue yes/no:

from random import choice
round_counter = 0
draw_count = 0
user_wins = 0
comp_wins = 0


def main():
    menu()


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
        round_to_play("a")
    elif user_m_choice == "d":
        game_difficulty()


def game_difficulty():
    print(f'You have a choice of difficulty.\nA - Smart (3 options - regular version)\nB - Stupid(5 options - '
          f'Sheldon\'s version)')
    diff = ""
    diff_options = ["a", "b", "q"]
    while diff.lower() not in diff_options:
        diff = input(f'What is Your choice -> ')
        if diff.lower() == "q":
            game_end(round_counter, user_wins, comp_wins, draw_count)
    round_to_play(diff.lower())


def round_to_play(diff):
    print(f'\nYou can chose how many rounds You want to play...')
    num_of_rounds = int(input('Type a number of rounds -> '))
    if diff == "a":
        game_a(num_of_rounds)
    elif diff == "b":
        game_b(num_of_rounds)


def game_a(num_of_rounds):
    print(f'Play {num_of_rounds} rounds of regular game')


def game_b(num_of_rounds):
    print(f'Play {num_of_rounds} rounds of stupid game')


def game_end(round_counter, user_wins, comp_wins, draw_count):
    """This function prints statistics and finish the game """
    user_decision = ""
    decision_options = ["y", "n"]
    while user_decision not in decision_options:
        user_decision = input(f'Would you like to continue yes/no: ')

    if round_counter == 0:
        print(f'Game Over')
    else:
        user_wins_percent = user_wins / round_counter * 100
        print(f'\nThere was {user_wins} round won by You, {comp_wins} rounds won by computer and {draw_count} draws.')
        print(f'You have won {user_wins_percent}% of rounds.')
        if user_wins == comp_wins:
            print(f'\nSo there was a draw in a whole game.')
        elif user_wins > comp_wins:
            print(f'\nSo You won the whole game.\n\nCongratulations!!!')
        elif user_wins < comp_wins:
            print(f'\nSo the computer won whole game.\n\nSorry!!!')


if __name__ == "__main__":
    main()
