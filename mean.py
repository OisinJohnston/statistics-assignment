from csvreader import read_csv



def mean(numbers):
    return sum(numbers)/len(numbers)


def main():
    rows = read_csv('frequency.csv')
    for row in rows:
        print(f'Mean: {mean(row)}')

    


if __name__ == '__main__':
    main()
