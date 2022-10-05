table = [
    ['Dorota', 'Wellman', 'journalist']
    ]
print(table)
print('--------------------------------------------------')
grades = {}.fromkeys(['Math', 'English', 'Art'], 3)
print(grades)
k = 'Math'
print(k in grades)
for key, value in grades.items():
    print(key, value)
stopnie = {}.fromkeys(['Polski', 'Matematyka', 'Geografia', 'Fizyka'], [3, 5, 4, 4])
for key, value in stopnie.items():
    print(key, value)

