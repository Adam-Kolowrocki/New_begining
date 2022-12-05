# Create a generator of any type, for e.g. generator of sentences, tweets or conferences.
# Input data from csv file, (csv file can be threatened as txt with known separator), which will contain data
# needed to generate.
with open('/home/adam/Dokumenty/Python-Kurs/New_beginning/07_File_operations/Data.csv', 'r') as data:
    data = data.readlines()

    print(data)
