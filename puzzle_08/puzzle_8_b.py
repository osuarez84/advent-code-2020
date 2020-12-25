import re

def get_file(file_name):
    with open(file_name, 'r') as f:
        list_el_file = [l.rstrip('\n') for l in f]
    return list_el_file



def check_loop(list_instructions):
    # Restart the variables
    index_instructions_already_visited = []
    accumulator = 0
    i = 0
    is_there_a_loop = False
    while (True):
        el = list_instructions[i]
        digits_match_and_op = re.search(r'([-+\d]+)', el, re.IGNORECASE)
        digits_and_op = digits_match_and_op.group(1)
        digits_match = re.search(r'([\d]+)', digits_and_op, re.IGNORECASE)
        if ('acc' in el):    
            if digits_match_and_op:
                #print(digits_and_op)
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
                    is_there_a_loop = True
                    break
                elif (i == len(list_instructions)):
                    # We have no loop in the program!!
                    break
                else:
                    index_instructions_already_visited.append(i)
                #print(index_instructions_already_visited)
        else:
            i += 1

    return is_there_a_loop, accumulator






def main():
    list_instructions = get_file('input.txt')
    
    #print(list_instructions)

    for instruction, idx in zip(list_instructions, range(0, len(list_instructions))):
        tmp_instruction = list_instructions[idx]
        digits_match_and_op = re.search(r'([-+\d]+)', list_instructions[idx], re.IGNORECASE)
        digits_and_op = digits_match_and_op.group(1)
        if ('nop' in instruction):
            list_instructions[idx] = 'jmp ' + digits_and_op
        elif ('jmp' in instruction):
            list_instructions[idx] = 'nop ' + digits_and_op

        # Execute the entire program to check whether there is a loop now
        is_there_a_loop, accumulator = check_loop(list_instructions)
        if (not is_there_a_loop):
            break

        # There is a loop!
        # recover the original value of the element and 
        # Check the next element
        list_instructions[idx] = tmp_instruction


    print(f'The value of the accumulator after the bug is fixed is {accumulator}.')

    return 0


# Iterate over every element of the program

# Change every element from jmp to nop or nop to jump
# and iterate over the entire program

# Check if an infinite loop is detected

# If detected undo the change to the instruction
# and pass to the next instruction


# If not detected then this was the bugged statement
# Check then the accumulator value



if __name__ == "__main__":
    main()