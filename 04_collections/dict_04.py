# Create multiplication table as a matrix size 10 x 10, filled with results of multiplications rows x columns.
for i in range(1, 11):
    multiplication = [1 * i]

# for row in range(1, 11):
#     for item in row:
#         multiplication = [item * row]
print(multiplication)


# print('\n'.join([''.join(['{:10}'.format(item) for item in row]) for row in range(1, 11)]))

# table_1 = [['x'] * n] * n