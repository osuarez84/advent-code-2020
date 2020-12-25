from itertools import combinations
import sys


def get_file(file_name):
    with open(file_name, 'r') as f:
        list_el_file = [l.rstrip('\n') for l in f]
    return list_el_file



def get_the_sum(s, e, l):

    # Get the window of numbers
    tmp_list = l[s:(e+1)]
    print(tmp_list)

    # Get al possible combinations in pairs inside the window
    comb = list(combinations(tmp_list, 2))

    print(comb)
    totals = list(map(lambda x: (x[0], x[1], sum(list(x))), comb))
    print(totals)

    return totals




def main():
    list_digits = get_file('input.txt')
    list_digits_int = list(map(int, list_digits))
    print(list_digits_int)

    for i in range(24, len(list_digits_int)):
        start = i - 24
        end = i
        list_triples = get_the_sum(start, end, list_digits_int)
        # Check first if the number exists in the total sum list
        list_totals = [j[2] for j in list_triples]

        # The number to check is the next of the i index => i+1
        print(list_digits_int[i+1])
        print(list_totals)
        if (list_digits_int[i+1] not in list_totals):
            print(f'The number that does not follow the XMAS encryption is: {list_digits_int[i+1]}')
            break

        triples_with_number = [n for n in list_triples if n[2] == list_digits_int[i+1]]
        print(triples_with_number)
        triples_with_no_rep_numbers = [n for n in triples_with_number if n[0] != n[1]]

        if (not triples_with_no_rep_numbers):
            print(f'The number that does not follow the XMAS encryption is: {list_digits_int[i+1]}')
            break


    return 0




if __name__ == "__main__":
    main()