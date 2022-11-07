table_3 = [
    [' ', '1', ' ', '2', ' ', '3'],
    ['A', '.', '|', '.', '|', '.'],
    ['B', '.', '|', '.', '|', '.'],
    ['C', '.', '|', '.', '|', '.'],
]
for i in range(len(table_3)):
    for j in range(len(table_3[i])):
        print(table_3[i][j], end=' ')
    print()
table_3[1][1] = 'X'
for i in range(len(table_3)):
    for j in range(len(table_3[i])):
        print(table_3[i][j], end=' ')
    print()
table_3[2][3] = 'O'
for i in range(len(table_3)):
    for j in range(len(table_3[i])):
        print(table_3[i][j], end=' ')
    print()
