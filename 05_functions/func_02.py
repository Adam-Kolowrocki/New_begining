# Write a function which check if given number is even.
def if_even(n):
    """This function check if number given by user is even."""
    if n % 2 == 0:
        return True
    else:
        return False


user_n = int(input(f'Type an integer number to be checked if it is even ->'))
print(f'The number "{user_n}" is even -> {if_even(user_n)}')
