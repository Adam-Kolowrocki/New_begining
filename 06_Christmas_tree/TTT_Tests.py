table_2 = [
    ['  1   2   3'],
    ['A . | . | .'],
    ['B . | . | .'],
    ['C . | . | .']
]
for col in table_2:
    for row in col:
        print(row, '\n', end='')

table_3 = [
    [' ', '1', ' ', '2', ' ', '3'],
    ['A', '.', '|', '.', '|', '.'],
    ['B', '.', '|', '.', '|', '.'],
    ['C', '.', '|', '.', '|', '.'],
]
# print(table_3[0])
# print(table_3[0][1])
# print(type(table_3[0][1]))
for col in table_3:
    i = 0
    while i in range(len(col)):
        print(col[i])
        i += 1
# for row in col:
# print(row)

# table_2[1][0].replace('A', 'X', 1)
# table_2[3][0].replace('.', 'O', 1)
# for row in table_2:
#       for col in row:
#             print(col, '\n', end='')
#
# print(type(table_2[2][0]))
