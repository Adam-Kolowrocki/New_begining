# Write script which given list split for 3 equal lists and turn away each one.
#  input: [1, 2, 3, 4, 11, 12, 13, 14, 21, 22, 23, 24]
#  output:
#  [4, 3, 2, 1]
#  [14, 13, 12, 11]
#  [24, 23, 22, 21]
given_list = [1, 2, 3, 4, 11, 12, 13, 14, 21, 22, 23, 24]
spliter = len(given_list) // 3
list_1 = given_list[0: spliter]
list_2 = given_list[spliter: spliter * 2]
list_3 = given_list[spliter * 2:]
list_1.reverse()
list_2.reverse()
list_3.reverse()
print(list_1)
print(list_2)
print(list_3)
