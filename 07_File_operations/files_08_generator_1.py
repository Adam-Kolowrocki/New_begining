# Create a generator of any type, for e.g. generator of sentences, tweets or conferences.
# Input data from csv file, (csv file can be threatened as txt with known separator), which will contain data
# needed to generate.
import csv
from random import choice


def main():
    """Main function - just print info"""
    print(f'This is a generator...'.center(100))
    print()
    print(f'It generates random quotes...'.center(100))
    print()
    input(f'Press [ENTER]')
    generator(*data_import())


# def data_import():
#     starts = [], middles, qualifiers, finishes = [], [], [], []
#     with open('./data3.csv') as file:
#         for i, line in enumerate(file):
#             first_coma = line.find(',')
#             second_coma = line.find(',', first_coma + 1, )
#             third_coma = line.find(',', second_coma + 1, )
#             starts.append(line[0: first_coma])
#             middles.append(line[first_coma + 1: second_coma])
#             qualifiers.append(line[second_coma + 1: third_coma])
#             finishes.append(line[third_coma + 1:])
#     return starts, middles, qualifiers, finishes
def data_import():
    starts = [], middles, qualifiers, finishes = [], [], [], []
    with open('./data3.csv') as file:
        for i, line in enumerate(file):
            first_coma = line.find(',')
            starts.append(line[0: first_coma])
            line = line[first_coma + 1:]
            second_coma = line.find(',')
            middles.append(line[0: second_coma])
            line = line[second_coma + 1:]
            third_coma = line.find(',')
            qualifiers.append(line[0: third_coma])
            line = line[third_coma + 1:]
            finishes.append(line[third_coma + 1:])
    return starts, middles, qualifiers, finishes

def generator(starts, middles, qualifiers, finishes):
    print(len(starts)), print(len(middles)), print(len(qualifiers)), print(len(finishes))
    print(starts[-3])
    print(middles[-3])
    print(qualifiers[-3])
    print(finishes[-3])
    print(choice(starts))
    print(choice(middles))
    print(choice(qualifiers))
    print(choice(finishes))
    quota = choice(starts) + ' ' + choice(middles) + ' ' + choice(qualifiers) + ' ' + choice(finishes)
    print(f'Generated quota is:\n{quota}')


if __name__ == "__main__":
    main()
