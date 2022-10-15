# To register a car as antique You have to fulfill next condition.
# The car have to be made in at least 75% from genuine parts.
# In this case we assume, that the expert determines it with Yes/No category.
# To Your dictionary add key: if_original with bool weight True/False.
# Print the dictionary again
#  Modify the code to check value of new key when Yuo try to register the car and return correct messages.
import datetime
cars_dic = {'mark': 'BMW',
            'model': '736',
            'vintage': '1998',
            'if_original': False
            }
actual_date = datetime.date.today().year


def beginning():
    """This function just inform user what the code does."""
    print(f'This is a vintage car registration program\n')
    print(f'Full dictionary -> {cars_dic}\n')


def car_check(cars_dic):
    """Check the values of dictionary to find out if a car is old enough to be antique."""
    if actual_date - int(cars_dic['vintage']) >= 25 and cars_dic["if_original"] is True:
        print(f'Congratulation! Your car {cars_dic["mark"]} {cars_dic["model"]} can be registered as antique.')
    elif actual_date - int(cars_dic['vintage']) >= 25 and cars_dic["if_original"] is False:
        print(f'Your car {cars_dic["mark"]} {cars_dic["model"]} is old enough, but it has too many new parts '
              f'to be registered as antique.')
    elif actual_date - int(cars_dic['vintage']) < 25 and cars_dic["if_original"] is True:
        print(f'Your car {cars_dic["mark"]} {cars_dic["model"]} is too young, but it is pretty original.')
    else:
        print(f'Your car {cars_dic["mark"]} {cars_dic["model"]} is too young and it has too many replaced parts '
              f'to be antique.')


beginning()
car_check(cars_dic)
