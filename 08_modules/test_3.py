import os

filename = 'inwokacja.txt'
if os.path.isfile(filename):
    with open(filename, 'r') as f:
        print(f.read())
else:
    print('Nie ma takiego pliku')
# with open("./Dokumenty/Python-Kurs/New_beginning/0")
