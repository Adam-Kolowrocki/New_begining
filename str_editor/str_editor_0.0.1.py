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
user_choice = input('Type ID numbers of OSD elements You want to delete:')
user_choice_labels = []
for j in range(len(user_choice)):
    user_choice_labels.append(choice_list[int(user_choice[j])-1])
print('You have chosen to delete:')
for k in range(len(user_choice_labels)):
    print(user_choice_labels[k])

print('druga linia ->', input_data[2])
# linie zawierajace info o parametrach lotu w pliku srt : 2, 6, 10, 14 itd

fl = len(input_data)
print('Plik wejsciowy ma lini ', fl)

for k in range(len(user_choice_labels)):
    delete_id = input_data[2].index(user_choice_labels[k])
    temp_str_2 = input_data[2]
    temp_beg, temp_end = temp_str_2[:delete_id], temp_str_2[delete_id:]
    space_id = temp_end.find(' ')
    temp_end = temp_end[space_id + 1:]
    input_data[2] = temp_beg + temp_end
    print('wiersz po zmianie', input_data[2])


def slicer(data):
    while fl <= fe:
        return
