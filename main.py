from csvreader import read_csv



def mean(numbers):
    return sum(numbers)/len(numbers)

def mode(numbers):
    frequency_map = {}
    for i in numbers:
        frequency_map[i] = frequency_map.get(i, 0) + 1
    biggest = 0
    for k, v in frequency_map.items():
        if v>biggest:
            biggest = v
    return [k for k, v in frequency_map.items() if v == biggest]


def median(numbers): 
    # TODO: finish this for hw
    pass




def main():
    rows = read_csv('frequency.csv')
    for row in rows:
        print(f'Mean: {mean(row)}')
        print(f'Mode: {mode(row)}')

    


if __name__ == '__main__':
    main()
