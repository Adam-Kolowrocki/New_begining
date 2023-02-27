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
sorted_list = []


def sorting_alpa(n_list):
    for j in range(len(n_list)):
        for k in range(len(n_list[j]) - 1):
            if n_list[j + 1][k] < n_list[j][k]:
                tmp = n_list[j + 1]
                n_list.pop((j + 1))
                n_list.insert(j, tmp)
    return n_list


sorting_alpa(names_list)
