#  Write a simple game, User have to guess a number from 0 to 20 hidden in the code,
#  (eg. secret_num = 5). Ask User till he guess.
print(f'This is a short game, try to guess a secret number from 0 to 20...')
secret_num = 7
user_num = int(input(f'Type Your number -> '))
while user_num != secret_num:
    print(f'\nYour number is incorrect...')
    user_num = int(input(f'Type Your number -> '))
print(f'\nCongratulations !!!')
print(f'You found the secret number which is "{user_num}".')
