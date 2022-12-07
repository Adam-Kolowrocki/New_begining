# Create a generator of any type, for e.g. generator of sentences, tweets or conferences.
# Input data from csv file, (csv file can be threatened as txt with known separator), which will contain data
# needed to generate.
import json

with open('./default_deepak_data.json') as json_file:
    data = json.load(json_file)
    print(data)
