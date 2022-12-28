def main():
    user_info()
    info_return(*bmi_calc(*data_input()))


def user_info():
    print('This simple code calculate Your BMI - Body Mass Index')
    print()
    print('Remember to use a dot "." as a separator...')
    print()


def data_input():
    """Collect data from user"""
    weight = float(input('What is Your weight in "kg" >> '))
    height = float(input('What is Your height in "m" >>'))
    return weight, height


def bmi_calc(weight, height):
    """Calculate BMI"""
    bmi_result = weight / (height ** 2)
    return bmi_result, weight, height


def info_return(bmi, weight, height):
    """Return info for the user"""
    print('If You are', height, 'm tall, and weight', weight, 'Your BMI is:', round(bmi, 2))
    if bmi <= 18.49:
        print('You are underweight.')
    elif 18.49 < bmi <= 24.99:
        print('Congratulations!!! Your weight is normal.')
    elif 24.99 < bmi <= 29.99:
        print('You are overweight.')
    else:
        print('You are obese. Be careful.')


if __name__ == '__main__':
    main()
