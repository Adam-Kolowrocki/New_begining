# str file editor for Walksnail digital FPV system
# helps to disable unwanted parts of standard Walksnail OSD info

with open('AvatarG0005.srt') as input_file:
    input_data = input_file.readlines()
print('STR file contains such data as:\n')
choice_list = input_data[2].split(' ')
for i in range(len(choice_list)):
    temp_str = choice_list[i]
    position = temp_str.find(':')
    choice_list[i] = temp_str[:position]
for i in range(len(choice_list)):
    print(i+1, '->', choice_list[i])
user_choice = input('Type numbers of OSD elements as shown in the list:')
user_choice_labels = []
for j in range(len(user_choice)):
    user_choice_labels.append(choice_list[int(user_choice[j])-1])
print('You have chosen to live in srt file objects as:')
for k in range(len(user_choice_labels)):
    print(user_choice_labels[k])
# print('zerowa linia ->', input_data[0])
# print('pierwsza linia ->', input_data[1])
print('druga linia ->', input_data[2])
print(type(input_data[2]))
# print('trzecia linia ->', input_data[3])
# print('czwarta linia ->', input_data[4])
# print('piata linia ->', input_data[5])
print('szosta linia ->', input_data[6])
print(type(input_data[6]))
# print('siodma linia ->', input_data[7])
# print('osma linia ->', input_data[8])
# print('dziewiata linia ->', input_data[9])
print('dziesiata linia ->', input_data[10])
print(type(input_data[10]))
