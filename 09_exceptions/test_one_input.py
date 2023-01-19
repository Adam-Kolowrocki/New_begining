user_input = ''
while len(user_input) != 1 or user_input.isalpha():
    user_input = input(f'Podaj dokładnie cyfrę ->')

print(f'User input wynosi {user_input} i ma długość {len(user_input)} znaków.')
user_input = int(user_input)
print(type(user_input))

