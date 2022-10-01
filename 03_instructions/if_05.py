# Create variable password. Password should contain at least 1 lowercase letter,
# at least 1 uppercase letter, numbers and be at least 8 characters long.
# If it is not, inform the user.
# Print different info for different errors in password.
print('This is the password checker...')
print('Type Your password to check.')
print('It should contain at least 1 uppercase and 1 lowercase letter'
      'at least 1 digit and be at least 8 characters long.')
password = input('Type Your password -> ')
if len(password) < 8 and password.isalpha() and password.islower():
    print('The password is to short, has no digits and uppercase letters.')
elif len(password) < 8 and password.isalpha() and password.isupper():
    print('The password is to short, has no digits and lowercase letters.')
elif len(password) < 8 and password.isdigit():
    print('The password is to short and has no letters.')
elif len(password) < 8 and password.isalpha():
    print('The password is to short and has no digits.')
elif len(password) < 8:
    print('The password is to short.')
elif password.isalpha() and password.islower():
    print('The password has no digits and uppercase letters.')
elif password.isalpha() and password.isupper():
    print('The password has no digits and lowercase letters.')
elif password.isdigit():
    print('The password has no letters.')
elif password.isalpha():
    print('The password has no digits.')
else:
    print('Congratulations. The password is strong.')
