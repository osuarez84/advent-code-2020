import sys
import re
import json

# This is a global variable used inside the recursion
can_contain = False

def get_file(file_name):
    with open(file_name, 'r') as f:
        list_el_file = [l.rstrip('\n') for l in f]
    return list_el_file


def tree_recursion(key, list_bags):
    global can_contain
    for i in list_bags[key]:
        if (i == 'shiny gold'):
            # If a the list of a key can follow a path to a shiny gold 
            # throughout multiple of the elements, we only need to count 
            # once , not once for every element.
            # for that pourpose we use a boolean variable that goes to True
            # if at least one element of the list can achieve shiny gold
            can_contain = True
            return
        else:
            tree_recursion(i, list_bags)


def main():
    global can_contain
    list_bags_raw = get_file('input.txt')

    # list_bags_raw = [
    #   'light red bags contain 1 bright white bag, 2 muted yellow bags.',
    #   'dark orange bags contain 3 bright white bags, 4 muted yellow bags.',
    #   'bright white bags contain 1 shiny gold bag.',
    #   'muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.',
    #   'shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.',
    #   'dark olive bags contain 3 faded blue bags, 4 dotted black bags.',
    #   'vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.',
    #   'faded blue bags contain no other bags.',
    #   'dotted black bags contain no other bags.'
    # ]

    starting_dict = {}
    ########
    # STEP 1
    ########
    # Prepare the dictionary with the keys as the root bag and a list with 
    # all the types of bags that it can include (extracting those from the rules
    # using regular expresions)
    for i in list_bags_raw:
        first_search = re.findall(r'^([\w\s]+)\sbags\scontain\s([^\.]+)', i)
        print(first_search)
        for j in first_search[0][1:]:
            second_search = re.findall(r'[0-9]+\s([a-z\s]+)\s(?:bag|bags)(?:,|$)', j)
            print(second_search)

        starting_dict[first_search[0][0]] = [i for i in second_search]
        
    print(json.dumps(starting_dict, indent=4))

    ########
    # STEP 2
    ########
    # Iterate over every key to check every list of bags inside it
    acc_sum = 0
    for key in starting_dict:
        tree_recursion(key, starting_dict)

        # If the key can at least achieve shiny gold with one element of the list
        # we know it using the boolean variable, so we increment the counter and 
        # set the boolean to false for the next element in the dict
        if(can_contain):
            acc_sum += 1
            can_contain = False

    print(acc_sum)
    return 0





if __name__ == "__main__":
    main()