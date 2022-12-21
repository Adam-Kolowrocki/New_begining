# File converter for Quota generator
with open('words_base.txt') as input_file:
    input_data = input_file.readlines()
for i in range(len(input_data)):
    input_data[i] = input_data[i].replace('        ', '').replace('"', '').replace(' ,\n', '').replace(',\n', '')

first_stop = input_data.index('\n')
second_stop = input_data.index('\n', first_stop + 3)
third_stop = input_data.index('\n', second_stop + 3)
starts, middles, qualifiers, finishes = input_data[0: first_stop], input_data[first_stop + 3: second_stop], \
                                        input_data[second_stop + 3: third_stop], input_data[third_stop + 3:]


with open('data3.csv', '+w') as new_data_csv:
    for i in range(len(finishes)):
        tmp_str = starts[i] + ',' + middles[i] + ',' + qualifiers[i] + ',' + finishes[i] + '\n'
        new_data_csv.write(tmp_str)
    for i in range(len(finishes), len(middles)):
        tmp_str = starts[i] + ',' + middles[i] + ',' + qualifiers[i] + '\n'
        new_data_csv.write(tmp_str)
    for i in range(len(middles), len(qualifiers)):
        tmp_str = starts[i] + ',' + qualifiers[i] + '\n'
        new_data_csv.write(tmp_str)
    for i in range(len(qualifiers), len(starts)):
        tmp_str = starts[i] + '\n'
        new_data_csv.write(tmp_str)
