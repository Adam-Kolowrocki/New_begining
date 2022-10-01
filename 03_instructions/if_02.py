# Ask user for two numbers, sum them.
# If the sum is grater then 100 - print it. Else print "End".
user_1 = int(input('Type firs integer number -> '))
user_2 = int(input('Type second integer number -> '))
print(f'Sum of Your numbers is grater then 100 and it is {user_1 + user_2}') if user_1 + user_2 > 100 else print('End')
