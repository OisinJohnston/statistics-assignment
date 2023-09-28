import csv

def read_csv(fp):
    with open(fp, newline='') as csvfile:
        reader = csv.reader(csvfile,  delimiter=',')
        return [[int(i) for i in row] for row in reader if row != []]


