# Write a program that will display successive results for the factorial of the natural number N
# (User-specified N, but not greater than 8).
print('Program returns result of factorial for given natural "n" not grater than 8.')
nat = int(input('Type natural number in range from 1 to 8:'))
if nat > 8:
    print('You give too big number.')
    nat = int(input('Type natural number in range from 1 to 8:'))
i = 1
s = 1
if nat == 0:
    print(f'{nat}! = 1')
elif nat == 1:
    print(f'{nat}! = 1')
else:
    print(f'{nat}! =')
for n in range(1, nat):
    print(n, end=' * ')
while i <= nat:
    s *= i
    i += 1
print(nat, '=', s)
print(f'Factorial of {nat} is equal {s}')
