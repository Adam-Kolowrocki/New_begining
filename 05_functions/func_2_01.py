# Use your bmi.py code. Divide counting bmi for function which count bmi on data from user
# and return correct value (underweight, normal weight, overweight, obesity) according to counted number.
print('This simple code calculate Your BMI - Body Mass Index')
print()
print('Remember to use a dot "." as a separator...')
print()


def bmi_calc(w, h):
    bmi = w / (h ** 2)
    return bmi


def bmi_info(bmi):
    print('If You are', height, 'm tall, and weight', weight, 'Your BMI is:', round(bmi, 2))
    if bmi < 18.5:
        print(f'Your BMi is to low, You are underweight.')
    elif 18.5 <= bmi < 25:
        print(f'Your BMi is ok, You are healthy.')
    elif 25 <= bmi < 30:
        print(f'Your BMi is to high, You are overweight.')
    else:
        print(f'Your BMi is much to high, You are obese.')


weight = float(input('What is Your weight in "kg" >> '))
height = float(input('What is Your height in "m" >>'))
bmi_info(bmi_calc(weight, height))
