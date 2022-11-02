# Write a game based on divination - Love Calc.
# Ask user about lovers names, count occurrence of each letter in both names and word LOVE.
# Reduce table by summ first and last number till there would be only two digits.
# The last two digits give the percentage of lovers matching.

def main():
    """The main function"""
    print(f'This is a short game to check percentage of lovers matching...\n')
    print(f'You give me Your names, I give You result...\n')
    input(f'Press any kay to continue...')
    name_collect()


def name_collect():
    """The function collects input data and returns string to be checked"""
    lover_1 = input(f'Type name of first lover ->')
    lover_2 = input(f'Type name of second lover ->')
    love_string = lover_1.lower() + 'love' + lover_2.lower()
    love_calc(love_string)


def love_calc(love_string):
    """This function count number of appearance of each letter in string"""
    love_number = []
    while len(love_string) > 0:
        love_number.append(love_string.count(love_string[0]))
        love_string = love_string.replace(love_string[0], '')
    love_percent(love_number)


def love_percent(x):
    """This function calculate and print match percentage"""
    if len(x) == 2:
        print(f'Lovers, Your match percent is = {x[0]}{x[1]}%.')
    else:
        y = []
        while len(x) > 1:
            y.append(x[0] + x[-1])
            x.pop(0)
            x.pop(-1)
            if len(x) == 1:
                y += x
        love_percent(y)


if __name__ == "__main__":
    main()
