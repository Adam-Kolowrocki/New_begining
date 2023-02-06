from random import randint
print(f'This is a short game.\nYou need to find a number from range 1 - 100.')
los = randint(1, 100)
odp = ''
i = 0

while odp != los:
    i += 1
    odp = int(input(f'Type Your number -> '))
    if odp < los:
        print(f'Your number is smaller than drawn number...')
    elif odp > los:
        print(f'Your number is higher than drawn number...')
print(f'Congratulations !!! You have guessed the number in {i} time.')
