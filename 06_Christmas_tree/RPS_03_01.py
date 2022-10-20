from random import choice
round_counter = 0
draw_count = 0
user_wins = 0
comp_wins = 0


def main():
    pass


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

if __name__ == "__main__":
    main()
