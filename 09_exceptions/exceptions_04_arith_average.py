# Count arithmetic average from few numbers. The numbers will be given by User separated by coma.
# Write a function which take the values and print average. The code should be resistant for user errors.
# Do not print the errors, write them to file.

user_numbers = input(f'Type as many numbers You want, separated with coma "," -> ')
user_num_list = []


def f_write(error):
    with open('errors.txt', 'a') as file:
        file.write(f'There was a {error}. \n')


def average():
    summ = 0
    for i in range(len(user_num_list)):
        summ += user_num_list[i]
    try:
        avg = summ / len(user_num_list)
    except ZeroDivisionError:
        f_write("ZeroDivisionError")
        exit()
    return avg


user_numbers = user_numbers.replace(" ", ",")
user_numbers = user_numbers.replace(".", ",")

try:
    if user_numbers[-1] != ",":
        user_numbers = user_numbers + ","
except IndexError:
    f_write("IndexError")

while len(user_numbers) > 0:
    idx = user_numbers.find(',')
    try:
        user_num_list.append(int(user_numbers[0: idx]))
    except ValueError:
        f_write("ValueError")
    user_numbers = user_numbers.removeprefix(user_numbers[0: idx + 1])
print(f'Average value of given number is = {average()}')
