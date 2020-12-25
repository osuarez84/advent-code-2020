import sys


def get_file(file_name):
    with open(file_name, 'r') as f:
        list_el_file = [l.rstrip('\n') for l in f]
    return list_el_file



def get_the_adjacent_values(row, col, seats_map):
    # Get all values from the seats next to the one
    # Init the values
    upper_center = None
    upper_left = None
    upper_right = None
    left = None
    right = None
    down_left = None
    down_center = None
    down_right = None
    
    #print(f'We begin in row {row} and col {col} with a {seats_map[row][col]}'.center(24))
    ############
    # UPPER LEFT
    ############
    if (row != 0 and col != 0):

        subtract_counter = 1
        while ((row-subtract_counter >= 0) and (col-subtract_counter >= 0)):
            upper_left = seats_map[row-subtract_counter][col-subtract_counter]
            #print(f'In row {row-subtract_counter} and col {col-subtract_counter} there is a {upper_left}')
            if ( (upper_left == 'L') or (upper_left == '#')):
                break
            else:
                subtract_counter += 1

        #print(f'Upper left-> Row: {row-subtract_counter}, column: {col-subtract_counter} contains a {upper_left}')

    #######
    # UPPER
    #######
    if (row != 0):
        subtract_counter = 1
        while (row-subtract_counter >= 0):
            upper_center = seats_map[row-subtract_counter][col]
            #print(f'In row {row-subtract_counter} and col {col} there is a {upper_center}')
            if ( (upper_center == 'L') or (upper_center == '#')):
                break
            else:
                subtract_counter += 1
        #print(f'Upper -> Row: {row-subtract_counter}, column: {col} contains a {upper_center}')

    #############
    # UPPER RIGHT
    #############
    if (row != 0 and col != len(seats_map[0])-1):
        subtract_counter = 1
        while ((row-subtract_counter >= 0) and (col+subtract_counter <= len(seats_map[0])-1)):
            upper_right = seats_map[row-subtract_counter][col+subtract_counter]
            #print(f'In row {row-subtract_counter} and col {col+subtract_counter} contains a {upper_right}.')
            if ((upper_right == 'L') or (upper_right == '#')):
                break
            else:
                subtract_counter += 1

        #print(f'Upper right -> Row: {row-subtract_counter}, column: {col+subtract_counter} contains a {upper_right}')

    ######
    # LEFT
    ######
    if (col != 0):
        subtract_counter = 1
        #left = seats_map[row][col-subtract_counter]
        while ((col-subtract_counter >= 0)):
            left = seats_map[row][col-subtract_counter]
            #print(f'In row {row} and col {col-subtract_counter} contains a {left}.')
            if ((left == 'L') or (left == '#')):
                break
            else:
                subtract_counter += 1
            
        #print(f'Left -> Row: {row}, column: {col-subtract_counter} contains a {left}')

    #######
    # RIGHT
    #######
    if (col != len(seats_map[0])-1):
        subtract_counter = 1
        while ((col+subtract_counter <= len(seats_map[0])-1)):
            right = seats_map[row][col+subtract_counter]
            #print(f'In row {row} and col {col+subtract_counter} contains a {right}.')
            if ((right == 'L') or (right == '#')):
                break
            else:
                subtract_counter += 1

        #print(f'Right -> Row: {row}, column: {col+subtract_counter} contains a {right}')

    ###########
    # DOWN LEFT
    ###########
    if (row != len(seats_map)-1 and col != 0):
        subtract_counter = 1
        while ((row+subtract_counter <= len(seats_map)-1) and ( col-subtract_counter >= 0)):
            down_left = seats_map[row+subtract_counter][col-subtract_counter]
            #print(f'In row {row+subtract_counter} and col {col-subtract_counter} contains a {down_left}.')
            if ((down_left == 'L') or (down_left == '#')):
                break
            else:
                subtract_counter += 1

        #print(f'Down left -> Row: {row+subtract_counter}, column: {col-subtract_counter} contains a {down_left}')

    #############
    # DOWN CENTER
    #############
    if (row != len(seats_map)-1):
        subtract_counter = 1
        while ((row+subtract_counter <= len(seats_map)-1)):
            down_center = seats_map[row+subtract_counter][col]
            #print(f'In row {row+subtract_counter} and col {col} contains a {down_center}')
            if ((down_center == 'L') or (down_center == '#')):
                break
            else:
                subtract_counter += 1

        #print(f'Down center -> Row: {row+subtract_counter}, column: {col} contains a {down_center}')

    ############
    # DOWN RIGHT
    ############
    if (col != len(seats_map[0])-1 and row != len(seats_map)-1):
        subtract_counter = 1
        while ((row+subtract_counter <= len(seats_map)-1) and (col+subtract_counter <= len(seats_map[0])-1)):
            down_right = seats_map[row+subtract_counter][col+subtract_counter]
            #print(f'In row {row+subtract_counter} and col {col+subtract_counter} contains a {down_right}')
            if ((down_right == 'L') or (down_right == '#')):
                break
            else:
                subtract_counter += 1
            
        #print(f'Down right -> Row: {row+subtract_counter}, column: {col+subtract_counter} contains a {down_right}')

    return  [upper_left, upper_center, upper_right, left, right, down_left, down_center, down_right]
    





def main():
    seats_map = get_file('input.txt')

    #seats_map_test = get_file('test_input.txt')

    # Init the previous iter map
    previous_iter_map = seats_map

    counter = 1
    while (True):
        print(f'Iteration number: {counter}')
        # Apply first rule
        next_iter_map = []
        for row in range(0, len(previous_iter_map)):
            tmp_col = ''
            for col in range(0, len(previous_iter_map[0])):
                #print(f'The value of the seat {row}.{col} is {seats_map[row][col]}')
                
                current_seat = previous_iter_map[row][col]

                list_adjacent_values_current_seat = get_the_adjacent_values(row, col, previous_iter_map)
                #print(f'Row {row} and col {col} has a list of adjacent: {list_adjacent_values_current_seat}')
                if (current_seat == '.'):
                    tmp_col = tmp_col + '.'
                elif (current_seat == 'L' and all(i != '#' for i in list_adjacent_values_current_seat)):
                    tmp_col = tmp_col + '#'
                else: # Otherwise the seat does not change
                    tmp_col = tmp_col + current_seat

            next_iter_map.append(tmp_col)

        #print(next_iter_map)

        with open('first_output_test.txt', 'w') as f:
            for x in next_iter_map:
                f.write(x + '\n')

        # Apply second rule
        second_iter_map = []
        for row in range(0, len(next_iter_map)):
            tmp_col = ''
            for col in range(0, len(next_iter_map[0])):

                current_seat = next_iter_map[row][col]

                list_adjacent_values_current_seat = get_the_adjacent_values(row, col, next_iter_map)

                if (current_seat == '.'):
                    tmp_col = tmp_col + '.'
                elif (current_seat == '#' and (list_adjacent_values_current_seat.count('#') >= 5)):
                    tmp_col = tmp_col + 'L'
                else:
                    tmp_col = tmp_col + current_seat
  
            second_iter_map.append(tmp_col)

        #print(second_iter_map)

        with open('second_output_test.txt', 'w') as f:
            for x in second_iter_map:
                f.write(x + '\n')

        # Check if the map of the current iteration is the same as the previous one
        if (previous_iter_map == second_iter_map):
            break

        # Refresh the previous iter map
        previous_iter_map = second_iter_map
        counter += 1

    #print(second_iter_map)


    # Count the number of occupied seats
    total = 0
    for i in second_iter_map:
        total += i.count('#')
    print(f'The number of occupied seats is: {total}')

    return 'ok'



if __name__ == "__main__":
    main()