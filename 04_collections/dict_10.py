# User gives random number N. Write a code which generate dictionary in which
# for every key N there is value of N*N
# So, if User gave N = 8
# Result : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
print(f'It will return a dictionary of given N and square of N')
user_number = int(input(f'Please, tape a number -> '))
n_dict = {}
for key in range(1, user_number + 1):
    n_dict[key] = key * key
print(n_dict)
