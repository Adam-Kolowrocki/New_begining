# town graph -> home - 0, school - 1, church - 2, pub - 3, hospital - 4, movie - 5, teatr - 6
town = [
    [0, 1, 1, 1, 0, 1, 0],
    [1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 1, 1, 0],
    [1, 0, 1, 0, 1, 0, 0],
    [0, 1, 1, 1, 0, 1, 1],
    [1, 0, 1, 0, 1, 0, 1],
    [0, 1, 0, 0, 1, 1, 1]
]
connection = 1
for row in enumerate(town):
    lst = row[1]
    for i in range(len(lst)):
        if lst[i] == 1:
            print(f'This is the connection nr {connection} -> ', row[0], "---", i)
            connection += 1
