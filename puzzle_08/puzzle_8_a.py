import re

def get_file(file_name):
    with open(file_name, 'r') as f:
        list_el_file = [l.rstrip('\n') for l in f]
    return list_el_file



def main():
    index_instructions_already_visited = []
    accumulator = 0

    list_instructions = get_file('input.txt')
    
    print(list_instructions)
    i = 0

    ########
    # PART A
    ########
    while (True):
        el = list_instructions[i]
        digits_match_and_op = re.search(r'([-+\d]+)', el, re.IGNORECASE)
        digits_and_op = digits_match_and_op.group(1)
        digits_match = re.search(r'([\d]+)', digits_and_op, re.IGNORECASE)

        if ('acc' in el):    
            if digits_match_and_op:
                print(digits_and_op)
                if ('+' in digits_and_op):
                    accumulator += int(digits_match.group(1))
                elif ('-' in digits_and_op):
                    accumulator -= int(digits_match.group(1))
                i += 1
        elif ('jmp' in el):
            if digits_match_and_op:
                if ('+' in digits_and_op):
                    i += int(digits_match.group(1))
                elif ('-' in digits_and_op):
                    i -= int(digits_match.group(1))
                
                if (i in index_instructions_already_visited):
                    print(f'The index that is repeated is {i}.')
                    print(f'The instruction with this index is {el}')
                    break
                else:
                    index_instructions_already_visited.append(i)
                print(index_instructions_already_visited)
        else:
            i += 1


    print(f'The value for the accumulator in the A part of the puzzle is {accumulator}.')

    return 0



if __name__ == "__main__":
    main()