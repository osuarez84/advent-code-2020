import re



ship_var = {
    'north': 0,
    'south': 0,
    'east': 0,
    'west': 0
}

# Waypoint unit coordinates relative to the ship
waypoint_var = {
    'north': 1,
    'south': 0,
    'east': 10,
    'west': 0
}



# N, S, E, W -> move the waypoint coords

# F -> move the ship times the waypoint coords

# L, R -> rotate the waypoint relative to the ship

def update_the_variables(s_dict, w_dict, order):
    # Get letter and number
    order_letter = re.findall(r'[A-Z]+', order)[0]
    order_number = re.findall(r'[0-9]+', order)[0]

    if (order_letter == 'N'):
        w_dict['north'] += int(order_number)
    elif (order_letter == 'S'):
        w_dict['south'] += int(order_number)
    elif (order_letter == 'E'):
        w_dict['east'] += int(order_number)
    elif (order_letter == 'W'):
        w_dict['west'] += int(order_number)
    elif (order_letter == 'F'):
        # Refresh all the ship coords
        s_dict['north'] += w_dict['north']*int(order_number)
        s_dict['south'] += w_dict['south']*int(order_number)
        s_dict['east'] += w_dict['east']*int(order_number)
        s_dict['west'] += w_dict['west']*int(order_number)
    elif (order_letter == 'L' or order_letter == 'R'):
        # TODO
        # adjust the waypoint coords relative to the ship
        
    return 





def get_file(file_name):
    with open(file_name, 'r') as f:
        list_el_file = [l.rstrip('\n') for l in f]
    return list_el_file



def main():
    movement_orders = get_file('input.txt')

    for order in movement_orders:
        update_the_variables(dict_variables, order)

    return 'ok'



if __name__ == "__main__":
    main()