# Rewrite bmi.py You made on first lesson, add "if" function,
# witch returns: underweight/normal weight/overweight/obese.
print('This simple code calculate Your BMI - Body Mass Index')
print()
print('Remember to use a dot "." as a separator...')
print()
weight = float(input('What is Your weight in "kg" >> '))
height = float(input('What is Your height in "m" >>'))
bmi = weight / (height ** 2)
print('If You are', height, 'm tall, and weight', weight, 'Your BMI is:', round(bmi, 2))
if bmi <= 18.49:
    print('You are underweight.')
elif 18.49 < bmi <= 24.99:
    print('Congratulations!!! Your weight is normal.')
elif 24.99 < bmi <= 29.99:
    print('You are overweight.')
else:
    print('You are obese. Be careful.')
