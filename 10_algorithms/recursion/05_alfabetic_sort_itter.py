# Sort list of names alfabetical.
# Input:
# In the first line of standard input there is a number of names N(1<= N <= 200).
# In the next lines there are names, one in each line.
# Names starts with capital letter, are max 50 characters long and contains of letters only.
# eg.
# 4
# Lipski
# Kowal
# Adamiak
# Wojtczak
# Output :
# Sorted names, each in new line.
# Adamiak
# Kowal
# Lipski
# Wojtczak
import time
names_list = []
with open("05_names.txt", "r") as file:
    names_count = int(file.readline())
    for i in range(names_count):
        names_list.append(file.readline())
print(f'\nImported list : \n')
for i in enumerate(names_list):
    print(i[0] + 1, "->", i[1].replace("\n", ""))
print(f'\nList sorted alfabetic : \n')
st = time.time()
print(names_list)
# alphabet = ABCDEFGHIJKLMNOPRSTUWXYZ
while


print(f'First pass')
for i in range(len(names_list) - 1):
    if names_list[i][0] < names_list[i + 1][0]:
        continue
    else:
        names_list[i], names_list[i + 1] = names_list[i + 1], names_list[i]
print(names_list)
print(f'Second pass')
for i in range(len(names_list) - 1):
    if names_list[i][0] < names_list[i + 1][0]:
        continue
    else:
        names_list[i], names_list[i + 1] = names_list[i + 1], names_list[i]
print(names_list)
print(f'Third pass')
for i in range(len(names_list) - 1):
    if names_list[i][0] < names_list[i + 1][0]:
        continue
    else:
        names_list[i], names_list[i + 1] = names_list[i + 1], names_list[i]
print(names_list)
print(f'Fourth pass')
for i in range(len(names_list) - 1):
    if names_list[i][0] < names_list[i + 1][0]:
        continue
    else:
        names_list[i], names_list[i + 1] = names_list[i + 1], names_list[i]
print(names_list)
print(f'Fifth pass')
for i in range(len(names_list) - 1):
    if names_list[i][0] < names_list[i + 1][0]:
        continue
    else:
        names_list[i], names_list[i + 1] = names_list[i + 1], names_list[i]
print(names_list)
print(f'Sixth pass')
for i in range(len(names_list) - 1):
    if names_list[i][0] < names_list[i + 1][0]:
        continue
    else:
        names_list[i], names_list[i + 1] = names_list[i + 1], names_list[i]
print(names_list)
print(f'Seventh pass')
for i in range(len(names_list) - 1):
    if names_list[i][0] < names_list[i + 1][0]:
        continue
    else:
        names_list[i], names_list[i + 1] = names_list[i + 1], names_list[i]
print(names_list)
print(f'Eight pass')
for i in range(len(names_list) - 1):
    if names_list[i][0] < names_list[i + 1][0]:
        continue
    else:
        names_list[i], names_list[i + 1] = names_list[i + 1], names_list[i]
print(names_list)
print(f'Ninth pass')
for i in range(len(names_list) - 1):
    if names_list[i][0] < names_list[i + 1][0]:
        continue
    else:
        names_list[i], names_list[i + 1] = names_list[i + 1], names_list[i]
print(names_list)
print(f'Tenth pass')
for i in range(len(names_list) - 1):
    if names_list[i][0] < names_list[i + 1][0]:
        continue
    else:
        names_list[i], names_list[i + 1] = names_list[i + 1], names_list[i]
print(names_list)


et = time.time()
print(f'Sorting of the list took = {et - st}s')
