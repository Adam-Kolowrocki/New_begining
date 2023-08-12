# str file editor for Walksnail digital FPV system
# helps to disable unwanted parts of standard Walksnail OSD info

with open('AvatarG0005.srt') as input_file:
    input_data = input_file.readlines()
print('STR file contains such data as:\n')
choice_list = input_data[2].split(' ')
for i in range(len(choice_list)):
    temp_str = choice_list[i]
    colon_idx = temp_str.find(':')
    choice_list[i] = temp_str[:colon_idx]
for i in range(len(choice_list)):
    print(i+1, '->', choice_list[i])
user_choice = input('Type ID numbers of OSD elements You want to delete:')
# if user_choice not in range(len(choice_list)+1):
#     print('You chosen wrong ID or do not want to delete any OSD item.')
# else:
user_choice_labels = []
for i in range(len(user_choice)):
    user_choice_labels.append(choice_list[int(user_choice[i])-1])
print('You have chosen to delete:')
for i in range(len(user_choice_labels)):
    print(user_choice_labels[i])

print('druga linia ->', input_data[2])
# linie zawierajace info o parametrach lotu w pliku srt : 2, 6, 10, 14 itd

fl = len(input_data)
print('Plik wejsciowy ma lini ', fl)

# for k in range(len(user_choice_labels)):
#     delete_id = input_data[2].index(user_choice_labels[k])
#     temp_str_2 = input_data[2]
#     temp_beg, temp_end = temp_str_2[:delete_id], temp_str_2[delete_id:]
#     space_id = temp_end.find(' ')
#     temp_end = temp_end[space_id + 1:]
#     input_data[2] = temp_beg + temp_end
#     print('wiersz po zmianie', input_data[2])
#
#
# def slicer(data):
#     while fl <= fe:
#         return

# ------------------------------------------------------------------------------
#
# input_data zawiera plik srt z napisami
# input_data[2] = Vbat:2.4v Signal:2 CH:5 Distance:30 -> linia pliku zawierająca wpisy (2, 6, 10, 14...)
# start_line = 2
# srt_end = len(input_data)
# info = ['Signal', 'CH', 'Distance']
# while start_line < srt_end:
# for y in range(len(info)):
# input_data[start_line] = clera(input_data[start_line], info[y])
# start_line = start_line + 4
#
# def clear(line, info):
# info_id = line.index(info) # index Distance w input_line[2]
# temp_beg = line[:info_id] # część wiersza input_line[2] od początku do wystąpienia
# elementu do usunięcia
# temp_end = line[info_id + 1:] # część wiersza input_line[2] od wystąpienia elementu do
# usunięcia do końca
# space_id = temp_end.index(‘ ‘) # index pierwszej spacji w temp_end
# temp_end = temp_end[space_id + 1:]
# line = temp_beg + temp_end
# return line
