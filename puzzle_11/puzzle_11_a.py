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
    # upper left
    if (row != 0 and col != 0):
        upper_left = seats_map[row-1][col-1]
        #print(f'Upper left: {upper_left}')
    # upper center
    if (row != 0):
        upper_center = seats_map[row-1][col]
        #print(f'Upper center: {upper_center}')
    # upper right
    if (row != 0 and col != len(seats_map[0])-1):
        upper_right = seats_map[row-1][col+1]
        #print(f'Upper right: {upper_right}')
    # left
    if (col != 0):
        left = seats_map[row][col-1]
        #print(f'Left: {left}')
    #right
    if (col != len(seats_map[0])-1):
        right = seats_map[row][col+1]
        #print(f'Right: {right}')
    # down left
    if (col != 0 and row != len(seats_map)-1):
        down_left = seats_map[row+1][col-1]
        #print(f'Down left: {down_left}')
    # down center
    if (row != len(seats_map)-1):
        down_center = seats_map[row+1][col]
        #print(f'Down center: {down_center}')
    # down right
    if (col != len(seats_map[0])-1 and row != len(seats_map)-1):
        down_right = seats_map[row+1][col+1]
        #print(f'Down right: {down_right}')

    return  [upper_center, upper_left, upper_right, left, right, down_left, down_center, down_right]
    





def main():
    seats_map = get_file('input.txt')

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

                if (current_seat == '.'):
                    tmp_col = tmp_col + '.'
                elif (current_seat == 'L' and all(i != '#' for i in list_adjacent_values_current_seat)):
                    tmp_col = tmp_col + '#'
                else: # Otherwise the seat does not change
                    tmp_col = tmp_col + current_seat

            next_iter_map.append(tmp_col)

        print(next_iter_map)

        # Apply second rule
        second_iter_map = []
        for row in range(0, len(next_iter_map)):
            tmp_col = ''
            for col in range(0, len(next_iter_map[0])):

                current_seat = next_iter_map[row][col]

                list_adjacent_values_current_seat = get_the_adjacent_values(row, col, next_iter_map)

                if (current_seat == '.'):
                    tmp_col = tmp_col + '.'
                elif (current_seat == '#' and (list_adjacent_values_current_seat.count('#') >= 4)):
                    tmp_col = tmp_col + 'L'
                else:
                    tmp_col = tmp_col + current_seat

            second_iter_map.append(tmp_col)

        print(second_iter_map)

        # Check if the map of the current iteration is the same as the previous one
        if (previous_iter_map == second_iter_map):
            break

        # Refresh the previous iter map
        previous_iter_map = second_iter_map
        counter += 1

    print(second_iter_map)


    # Count the number of occupied seats
    total = 0
    for i in second_iter_map:
        total += i.count('#')
    print(f'The number of occupied seats is: {total}')

    return 'ok'



if __name__ == "__main__":
    main()