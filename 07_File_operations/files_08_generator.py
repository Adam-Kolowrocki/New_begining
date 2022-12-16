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


def data_import():
    """Imports data from *.csv file and splits it for lists."""
    with open('./data4.csv') as file:
        starts = []
        middles = []
        qualifiers = []
        finishes = []
        for line in file.readlines():
            first_coma = line.find(',')
            starts.append(line[0: first_coma])
            line = line[first_coma + 1:]
            second_coma = line.find(',')
            middles.append(line[0: second_coma])
            line = line[second_coma + 1:]
            third_coma = line.find(',')
            qualifiers.append(line[0: third_coma])
            line = line[third_coma + 1:]
            finishes.append(line)
    return starts, middles, qualifiers, finishes


def generator(starts, middles, qualifiers, finishes):
    """Generate quote from words/frazes in lists."""
    quota = choice(starts) + ' ' + choice(middles) + ' ' + choice(qualifiers) + ' ' + choice(finishes)
    print(f'Generated quota is:\n{quota}')


if __name__ == "__main__":
    main()
