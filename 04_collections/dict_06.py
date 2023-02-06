# Create a list containing values dictionary below with no duplicates.
# days = {'Jan': 31, 'Feb': 28, 'Mar': 31, 'Apr': 30, 'May': 31, 'Jun': 30, 'Jul': 31, 'Aug': 31, 'Sept': 30}
days = {'Jan': 31, 'Feb': 28, 'Mar': 31, 'Apr': 30, 'May': 31, 'Jun': 30, 'Jul': 31, 'Aug': 31, 'Sept': 30}
list_tmp = []
for k in days:
    list_tmp.append(days[k])
list_tmp = set(list_tmp)
list_tmp = list(list_tmp)
print(f'List of non duplicated values from dictionary "days" is = {list_tmp}.')
