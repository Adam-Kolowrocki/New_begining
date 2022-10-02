prime_numbers = []
for current_num in range(2, 10):
    for x in range(2, current_num):
        if current_num % x == 0:
            print(current_num, 'is divided by', x)
            #print(current_num, 'equals', current_num, '*', current_num // x)
            # znaleziono dzielnik!!! - możemy przejść do kolejnej cuurrent_num
            # pomijając sprawdzanie x
            break
        else:
            # nie znaleziono dzielnika
            print(current_num, 'can\'t be divided by', x)
            prime_numbers.append(current_num)
prime_numbers = set(prime_numbers)
print(f'Prime numbers from 2 to 10 are -> {prime_numbers}')

for val in "string":
    if val == "i":
        break
    print(val)
print("Koniec")

for val in "string":
    if val == "i":
        print('lalala')
        continue
    print(val)

print("Koniec")
for val in "string":
    if val == "i":
        print('lalala')
    print(val)

print("Koniec")
