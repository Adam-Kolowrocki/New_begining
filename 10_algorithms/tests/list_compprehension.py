list_1 = list(range(11))
list_2 = [i * 2 for i in list_1]
list_3 = [i + 2 for i in list_1 if i % 2 == 0]
print(f'First list : {list_1}')
print(f'Second list - multiplication : {list_2}')
print(f'Third list - addition to even elements : {list_3}')

# string formatting

arg = ["Adam", 41, "build and fly drones"]
test_str = "Hi, my name is {name}, I'm {age} years old and i like to {hobby}.".format(
    name=arg[0], age=arg[1], hobby=arg[2])
print(test_str)

print("-------------------------------------------------")
print(", ".join(["a", "b", "c"]))
print("Hello Word".replace("Hello", "Zdrastwuj"))
print("This is a sentence.".startswith("This"))
print("This is a sentence.".startswith("thi"))
print("This is a sentence.".endswith("."))
print("This is a sentence.".endswith(","))
print("X" in "This is a sentence.")
print("This is a sentence.".upper())
print("This is a sentence.".lower())
print("===================================")
list_4 = [10, 20, 25, 35, 40]

if all([i % 2 == 0 for i in list_4]):
    print('All numbers in lista_4 are even..')
else:
    print('Not all numbers in lista_4 are even..')

if any([i % 2 == 0 for i in list_4]):
    print('At least one number in lista_4 is even...')

for i in enumerate(list_4):
    print(i[0] + 1, "->", i[1])
