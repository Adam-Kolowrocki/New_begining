# Create 2D table (in code), which contain personal data as in example:
#     Dorota, Wellman, journalist
#     Adam, Małysz, sportsmen
#     Robert, Lewandowski, football player
#     Krystyna, Janda, actor
# Print in som nice way, easy to read for user.
table = [
    ['Dorota', 'Wellman', 'journalist'],
    ['Adam', 'Małysz', 'sportsman'],
    ['Robert', 'Lewandowski', 'football player'],
    ['Krystyna', 'Janda', 'actor']
    ]
print(f'There are four rows in table with names and occupations.')
var_x = int(input(f'Which one do You want to be familiar with ->'))
first_name = table[var_x - 1][0]
surname = table[var_x - 1][1]
occupation = table[var_x - 1][2]
print(f'Name {first_name}, surname {surname}, works as {occupation}.')
