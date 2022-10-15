# Write a game hot - cold using functions.
from random import randint


def secret_num():
    """Function generate secret number from range 0-100"""
    secret_number = randint(0, 100)
    return secret_number


def game_body(s_number):
    """Function compare secret number with number given by user and returns specific info"""
    secret_number = s_number
    round_counter = 0
    while round_counter < 6:
        round_counter += 1
        user_number = int(input(f'Type Your number -> '))
        if user_number == secret_number:
            print(f'Congratulation !!!\nYou have won the game.')
        elif user_number in range(secret_number - 10, secret_number + 10):
            print(f'HOT')
        elif user_number in range(secret_number - 20, secret_number + 20):
            print(f'Warm')
        else:
            print(f'Cold')


def info():
    """Begining info"""
    print(f'It is a game Hot/Cold.')
    print(f'You have to guess a secret number in range from 0 to 100.')
    print(f'I will try to help You giving advices - "hot", "warm" and "cold".')
    print(f'But remember, You have only 6 attempts.')


info()
game_body(secret_num())


print(f'You did not found the number in 6 attempts.\nYou have loose...')
