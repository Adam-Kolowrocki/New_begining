# Write a function which will check if the number is in the range given by user.
# It should return info : "Yes, number X is in the given range.", “no, the number X is out of given range."

def usr_range():
    low_end = int(input(f'What is the low end of the range -> '))
    high_end: int = int(input(f'What is the high end of the range -> '))
    while low_end > high_end:
        print(f'You gave wrong range numbers.\n')
        low_end = int(input(f'What is the low end of the range -> '))
        high_end: int = int(input(f'What is the high end of the range -> '))
        continue
    return low_end, high_end


def range_check(low, high):
    x = 18
    if low <= x <= high:
        print(f'Yes, number {x} is in the given range. X = {x}')
    else:
        print(f'No, the number X is out of given range.')


print(f'This code checks if the constant number "x" is in the range given by user.')
low, high = usr_range()

range_check(low, high)
