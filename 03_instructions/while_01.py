# Write a code transferring Fahrenheit for Celsius.
# It should operate in a loop from 0 to 200 Fahrenheit for every 20 degree.
#     C = 5/9 * (F - 32) # Celsjusz → Fahrenheit
# Write it with "while" as well as "for" loop.
f_d = 0
c_d = 0
while f_d <= 200:
    c_d = round((5 / 9) * (f_d - 32), 2)
    print(f'{f_d}F = {c_d}C')
    f_d += 20
