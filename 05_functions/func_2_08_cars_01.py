# Write a program which will check if the car could be registered as antique.
# Starts with dictionary of 3 keys:
#  mark (str)
#  model (str)
#  vintage (int)
# Print the dictionary without formatting.
# Check if the car is at least 2 years old, if so, print:
#         “Congratulation! Your car (mark) can be registered as antique.“
# If it doesn't print:
#         “Your car (mark) is too young.”
# When the codr will work properly, change dictionary values (but no keys), to check if it works ok with other input.
import datetime
cars_dic = {'mark': 'BMW',
            'model': '736',
            'vintage': '1978'
            }
actual_date = datetime.date.today().year


def beginning():
    """This function just inform user what the code does."""
    print(f'This is a vintage car registration program\n')
    print(f'Full dictionary -> {cars_dic}\n')


def car_check(cars_dic):
    """Check the values of dictionary to find out if a car is old enough to be antique."""
    if actual_date - int(cars_dic['vintage']) >= 25:
        print(f'Congratulation! Your car {cars_dic["mark"]} {cars_dic["model"]} can be registered as antique.')
    else:
        print(f'Your car {cars_dic["mark"]} {cars_dic["model"]} is too young.')


beginning()
car_check(cars_dic)
