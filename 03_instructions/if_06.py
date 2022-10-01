# Ask user for a number from 1 to 100, if he will guess the number hidden by developer,
# print "Congratulations" otherwise print "You mist".
secret_number = 57
user_number = int(input('Type an integer number from 1 to 100 -> '))
if user_number == secret_number:
    print('Congratulations, You have found the secret number!!!')
else:
    print('You have mist...')
