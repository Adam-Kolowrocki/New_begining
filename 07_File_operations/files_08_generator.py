# Create a generator of any type, for e.g. generator of sentences, tweets or conferences.
# Input data from csv file, (csv file can be threatened as txt with known separator), which will contain data
# needed to generate.
with open('/home/adam/Dokumenty/Python-Kurs/New_beginning/07_File_operations/data1.csv', 'r') as data:
    data = data.readlines()
    for i in range(len(data)):
        data[i] = data[i].replace('"', '')
        data[i] = data[i].replace('\n', '')
first_stop = data.index('----')
second_stop = data.index('----', first_stop + 1)
third_stop = data.index('----', second_stop + 1)
starts = data[0: first_stop]
middles = data[first_stop + 1: second_stop]
qualifiers = data[second_stop + 1: third_stop]
finishes = data[third_stop + 1:]
with open('data2.csv', '+w') as new_data_csv:
    for i in range(len(starts)):
        tmp_str = starts[i] + middles[i] + qualifiers[i] + finishes[i] + '\n'
        new_data_csv.write(tmp_str)
