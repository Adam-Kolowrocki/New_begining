# Count arithmetic average from few numbers. The numbers will be given by User separated by coma.
# Write a function which take the values and print average. The code should be resistant for user errors.
# Do not print the errors, write them to file.

# user_numbers = input(f'Type as many numbers You want, separated with coma "," -> ')
# user_numbers = "'k',23,'lk',65,12,98,'fd',34,'op'"
user_numbers = "sfsdf 3434 344 dsafds"
user_num_list = []


def f_write(error):
    with open('errors.txt', 'a') as file:
        file.write(f'There was a {error}. \n')


# try:
#     if user_numbers[-1] != ",":
#         user_numbers = user_numbers + ","
# except IndexError:
#     f_write("IndexError")

if user_numbers.find(",") == -1:
    if user_numbers.find(" "):
        user_numbers.replace(" ", ",")
        exit()
    elif user_numbers.find("."):
        print('są kropki')
        user_numbers.replace(".", ",")
    else:
        print(f'There is no separator sign I could recognize...')
        print(f'The program will end.')
        exit()

while len(user_numbers) > 0:
    print(user_numbers)
    idx = user_numbers.find(',')
    try:
        user_num_list.append(int(user_numbers[0: idx]))
    except ValueError:
        f_write("ValueError")
    user_numbers = user_numbers.removeprefix(user_numbers[0: idx + 1])


def average():
    summ = 0
    for i in range(len(user_num_list)):
        summ += user_num_list[i]
    try:
        avg = summ / len(user_num_list)
    except ZeroDivisionError:
        f_write("ZeroDivisionError")
        print('jestem 5')
        exit()
    return avg


print('jestem 4')
print(f'Average value of given number is = {average()}')
