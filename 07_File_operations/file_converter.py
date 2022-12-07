# Create a generator of any type, for e.g. generator of sentences, tweets or conferences.
# Input data from csv file, (csv file can be threatened as txt with known separator), which will contain data
# needed to generate.
with open('words_base.txt') as input_file:
    input_data = input_file.readlines()
for i in range(len(input_data)):
    input_data[i] = input_data[i].replace('        ', '')
    input_data[i] = input_data[i].replace('"', '')
    input_data[i] = input_data[i].replace(' ,\n', '')
print(input_data)

first_stop = input_data.index('\n')
second_stop = input_data.index('\n', first_stop + 3)
third_stop = input_data.index('\n', second_stop + 3)
starts = input_data[0: first_stop]
middles = input_data[first_stop + 3: second_stop]
qualifiers = input_data[second_stop + 3: third_stop]
finishes = input_data[third_stop + 3:]
for i in range(len(finishes)):
    finishes[i] = finishes[i].replace(',\n', '')
print(f'{len(starts)} = starts = {starts}')
print(f'{len(middles)} = middles = {middles}')
print(f'{len(qualifiers)} = qualifiers {qualifiers}')
print(f'{len(finishes)} = finishes = {finishes}')
with open('data3.csv', '+w') as new_data_csv:
    for i in range(len(starts)):
        tmp_str = starts[i] + ',' + middles[i] + ',' + qualifiers[i] + ',' + finishes[i] + '\n'
        new_data_csv.write(tmp_str)
