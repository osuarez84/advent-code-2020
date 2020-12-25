from itertools import combinations
import sys


def get_file(file_name):
    with open(file_name, 'r') as f:
        list_el_file = [l.rstrip('\n') for l in f]
    return list_el_file



def main():

    invalid_number = 1930745883

    list_digits = get_file('input.txt')
    list_digits_int = list(map(int, list_digits))
    #print(list_digits_int)

    for i in range(0, len(list_digits_int)):
        for j in range(i+1, len(list_digits_int)):
            numbers = list_digits_int[i:j+1]
            #print(numbers)
            total = sum(numbers)
            #print(f'Total for numbers {numbers} is {total}.')
            if (total == invalid_number):
                print(f'The numbers that sums {invalid_number} are {numbers}.')
                small_number = min(numbers)
                higher_number = max(numbers)
                print(f'The encryption weakness is {small_number+higher_number}.')
                break


    return 0



if __name__ == "__main__":
    main()