from bmi import bmi_calc


def main():
    info_return(*bmi_calc(*data_collect()))


def data_collect():
    print(f'Remember to use dot "." as a separator')
    weight = float(input(f'What is Your weight in "kg" >> '))
    height = float(input('What is Your height in "m" >> '))
    return weight, height


def info_return(bmi, weight, height):
    """Return info for the user"""
    print(f'If You are {height}m tall and weight {weight}kg, Your BMI is: {bmi}')
    with open('../advices.txt', 'r') as f:
        if bmi <= 18.49:
            print(f.readlines()[0])
        elif 18.49 < bmi <= 24.99:
            print(f.readlines()[1])
        elif 24.99 < bmi <= 29.99:
            print(f.readlines()[2])
        else:
            print(f.readlines()[3])


if __name__ == "__main__":
    main()
