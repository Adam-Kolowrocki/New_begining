# Check if given string is a palindrom.
given_string = input('Type a string to be checked if it is a palindrom -> ')
given_string = given_string.replace(" ", "")
print('Your string is a palindrom -', given_string == given_string[::-1])
