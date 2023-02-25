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
for i in enumerate(sorted(names_list)):
    print(i[0] + 1, "->", i[1].replace("\n", ""))
et = time.time()
print(f'Sorting of the list took = {et - st}s')
