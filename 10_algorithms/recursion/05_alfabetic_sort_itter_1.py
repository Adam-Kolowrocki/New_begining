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
print(f'\nList sorted alphabetic : \n')
st = time.time()
i = 0
while i < len(names_list):
    for j in range(i + 1, len(names_list)):
        if names_list[j][0] == names_list[i][0]:
            if names_list[j][1] == names_list[i][1]:
                if names_list[j][2] == names_list[i][2]:
                    if names_list[j][3] < names_list[i][3]:
                        tmp_3 = names_list[j]
                        names_list.pop(j)
                        names_list.insert(i, tmp_3)
                elif names_list[j][2] < names_list[i][2]:
                    tmp_2 = names_list[j]
                    names_list.pop(j)
                    names_list.insert(i, tmp_2)
            elif names_list[j][1] < names_list[i][1]:
                tmp_1 = names_list[j]
                names_list.pop(j)
                names_list.insert(i, tmp_1)
        elif names_list[j][0] < names_list[i][0]:
            tmp = names_list[j]
            names_list.pop(j)
            names_list.insert(i, tmp)
    i += 1
et = time.time()
for i in enumerate(names_list):
    print(i[0] + 1, "->", i[1].replace("\n", ""))
print(f'Sorting of the list took = {et - st}s')
