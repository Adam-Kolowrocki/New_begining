# Create table n x n containing random sign, then print it as a table n x n.
# Elements should be separated with space.
n = 4
table_1 = [['x'] * n] * n
table_n = [['x', 'x', 'x', 'x'],
           ['x', 'x', 'x', 'x'],
           ['x', 'x', 'x', 'x'],
           ['x', 'x', 'x', 'x']]
print(table_1)
print(table_n)
print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in table_1]))
print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in table_n]))
