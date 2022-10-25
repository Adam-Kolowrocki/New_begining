from random import choice


def game_a():
    num_of_rounds = 15
    round_counter, user_wins, comp_wins, draw_count = 0, 0, 0, 0
    print(f'Play {num_of_rounds} rounds of regular game')
    while round_counter < num_of_rounds:
        options = 'r', 'p', 's'
        print(f'\nYou can chose one of "r" as for rock, "p" as for paper or "s" as for scissors.')
        user_choice = input(f'\nWhat is Your choice -> ').lower()
        if user_choice == 'q':
            print(f'Player ended the game')
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
        elif (comp_choice == "r" and user_choice == "p") or (comp_choice == "p" and user_choice == "s") or \
                (comp_choice == "s" and user_choice == "r"):
            print(f'You chose "{user_choice}" and computer choose "{comp_choice}".')
            print(f'You have won.')
            user_wins += 1
        elif (comp_choice == "r" and user_choice == "s") or (comp_choice == "p" and user_choice == "r") or \
                (comp_choice == "s" and user_choice == "p"):
            print(f'You chose "{user_choice}" and computer choose "{comp_choice}".')
            print(f'The computer won.')
            comp_wins += 1
        # elif comp_choice == "p" and user_choice == "r":
        #     print(f'You chose "{user_choice}" and computer choose "{comp_choice}".')
        #     print(f'The computer won.')
        #     comp_wins += 1
        # elif comp_choice == "p" and user_choice == "s":
        #     print(f'You chose "{user_choice}" and computer choose "{comp_choice}".')
        #     print(f'You have won.')
        #     user_wins += 1
        # elif comp_choice == "s" and user_choice == "p":
        #     print(f'You chose "{user_choice}" and computer choose "{comp_choice}".')
        #     print(f'The computer won.')
        #     comp_wins += 1
        # elif comp_choice == "s" and user_choice == "r":
        #     print(f'You chose "{user_choice}" and computer choose "{comp_choice}".')
        #     print(f'You have won.')
        #     user_wins += 1
    print(f'User wins {user_wins} times, comp wins {comp_wins} times, there was {draw_count} draws and '
          f'{round_counter} rounds.')
    return user_wins, comp_wins, draw_count, round_counter


game_a()
