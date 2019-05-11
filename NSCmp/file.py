import csv
from operator import itemgetter

filename = 'smile_records.csv'

def read_coordinates(filename):
    coordinates = list(csv.reader(open(filename)))
    header = coordinates[0]
    sorted_items = sorted(coordinates[:5], key=itemgetter(0))
    sorted_coordinates = [header] + sorted_items
    return sorted_coordinates

def print_table(table):
    for column in table[:5]:
        lines = ['{}: {}'.format(table[0][i],v) for i, v in enumerate(column)]
        string = '\n'.join(lines)
        print (string, '\n')

def main (filename):
    coordinates = read_coordinates(filename)
    ratio = float ((((column[3])/(column[2])) + ((column[5])/(column[4])))/2)

    print ('ratio= ', ratio)

if __name__ == '__main__':
    main('smile_records.csv')