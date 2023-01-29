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
for row in enumerate(town):
    print(row)
    # for col in enumerate(row):
        # if row[col] == 1:
            # print(row[col])
# for row in town:
#     for col in row:
#         if row[col] == 1:
#             print(town[row], "---", row[col])
