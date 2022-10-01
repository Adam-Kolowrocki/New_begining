# Ask user for 3 numbers.
# Check if user number is divisble by 3
# print "It is divisible by 3".

user_num = int(input('Type an intiger number -> '))
if user_num % 3 == 0:
    print('Your number is divisible by 3.')
else:
    print("Your number isn't divisible by 3.")
