import os
file_name = input(f'Type a file to import -> ')
if '/' not in file_name:
    file_name = '/home/adam/Dokumenty/Python-Kurs/Files/' + file_name
else:
    file_name = file_name
with open(file_name, 'r') as inwo:
    lines = inwo.readlines()
    for i in range(5):
        print(f'Line {i + 1} : {lines[i]}')

print(f'The file You point is {os.path.getsize(file_name)} bytes long.')
