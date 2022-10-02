# In a string given by User count: smal letters, big letters, digits and special signs.
user_string = input('Type Your string to process -> ')
small = 0
big = 0
digits = 0
special = 0
for sign in user_string:
    if sign.islower():
        small += 1
    elif sign.isupper():
        big += 1
    elif sign.isdigit():
        digits += 1
    else:
        special += 1
print(f'There are - {small} - small letters in given string.')
print(f'There are - {big} - big letters in given string.')
print(f'There are - {digits} - digits in given string.')
print(f'There are - {special} - special signs in given string.')
