# Create 2 tuples. Then create a list which contain elements with even index from one tuple and not even from second.
# Translate the list into set.
tuple_2 = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k')
tuple_3 = ('l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'x', 'y', 'z')
list_1 = []
for i in range(0, len(tuple_2)):
    if i % 2 != 0:
        list_1.append(tuple_2[i])
for i in range(0, len(tuple_3)):
    if i % 2 == 0:
        list_1.append(tuple_3[i])
print('Lista wygląda tak -> ', list_1)
set_2 = set(list_1)
print('Set wygląda tak -> ', set_2)
