# Take 10 numbers from user, print only not even.
user_numbers = input(f'Please, type 10 numbers separated with coma "," -> ')
user_numbers = user_numbers.split(",")
not_even_num = []
for num in user_numbers:
    num = int(num)
    if num % 2 != 0:
        not_even_num.append(num)
print(f'From given numbers only "{not_even_num}" are not even')
