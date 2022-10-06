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

print('================================================')
txt = "For only {price:.2f} dollars!"
print(txt.format(price=49))
txt1 = "My name is {fname}, I'm {age}".format(fname="John", age=36)
txt2 = "My name is {0}, I'm {1}".format("John", 36)
txt3 = "My name is {}, I'm {}".format("John", 36)
print(txt1)
print(txt2)
print(txt3)
print('####################################################')
for n in range(11):
    print(1 * n)
