# Write a function which will check if the number is in the range given by user.
# It should return info : "Yes, number X is in the given range.", “no, the number X is out of given range."

def usr_range():
    low_end = int(input(f'What is the low end of the range -> '))
    high_end = int(input(f'What is the high end of the range -> '))
    return low_end, high_end


def range_check(low, high):
    x = 18
    if low > high:
        print(f'You gave wrong range numbers.')
        usr_range()
    elif low <= x <= high:
        print(f'Yes, number {x} is in the given range.')
    else:
        print(f'No, the number X is out of given range.')


print(f'This code checks if the constant number "x" is in the range given by user.')
range_check(low=usr_range()[0], high=usr_range()[1])
