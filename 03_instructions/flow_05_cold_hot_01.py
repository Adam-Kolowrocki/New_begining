# Write a game hot / cold.
#   Computer pick a random number from 0 to 100.
#   User give his number.
#   Computer return hot / cold, no more than 6 times.
#   If User guess the number, He wins.
#   If after 6 attempts User do not guess - computer wins.
from random import randint
secret_number = randint(0, 100)
round_counter = 0
print(f'It is a game Hot/Cold.')
print(f'You have to guess a secret number in range from 0 to 100.')
print(f'I will try to help You giving advices - "hot", "warm" and "cold".')
print(f'But remember, You have only 6 attempts.')
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
print(f'You did not found the number in 6 attempts.\nYou have loose...')
