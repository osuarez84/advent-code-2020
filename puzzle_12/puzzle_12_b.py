import re



ship_var = {
    'north': 0,
    'south': 0,
    'east': 0,
    'west': 0
}


waypoint_var = {
    'x': 10,
    'y': 1,
    'angle_relative_to_start': 0

}


# N, S, E, W -> move the waypoint coords

# F -> move the ship times the waypoint coords

# L, R -> rotate the waypoint relative to the ship

def update_waypoint(d, o_l, o_n):
    print('Updating waypoint!')
    if (o_l == 'N'):
        d['y'] += int(o_n)
    elif (o_l == 'S'):
        d['y'] -= int(o_n)
    elif (o_l == 'E'):
        d['x'] += int(o_n)
    elif (o_l == 'W'):
        d['x'] -= int(o_n)
    elif (o_l == 'L' or o_l == 'R'):
        d['angle_relative_to_start'] = ((d['angle_relative_to_start'] - int(o_n)) % 360 )if o_l == 'L' else ((d['angle_relative_to_start'] + int(o_n)) % 360)
        # Update the sign of the x , y coordinates
        if (d['angle_relative_to_start'] == 0):
            d['x'], d['y'] = abs(d['x']), abs(d['y'])
        elif (d['angle_relative_to_start'] == 90):
            d['x'], d['y'] = abs(d['y']), -d['x']
        elif (d['angle_relative_to_start'] == 180):
            d['x'], d['y'] = -d['x'], -d['y']
        elif (d['angle_relative_to_start'] == 270):
            d['x'], d['y'] = -d['y'], abs(d['x'])


def update_ship(d_s, d_w, o_n):
    # Refresh all the ship coords
    print('Updating ship!')
    if (d_w['y'] > 0):
        d_s['north'] += abs(d_w['y'])*int(o_n)
    else:
        d_s['south'] += abs(d_w['y'])*int(o_n)

    if (d_w['x'] > 0):
        d_s['east'] += abs(d_w['x'])*int(o_n)
    else:
        d_s['west'] += abs(d_w['x'])*int(o_n)

def update_the_variables(s_dict, w_dict, order):
    # Get letter and number
    order_letter = re.findall(r'[A-Z]+', order)[0]
    order_number = re.findall(r'[0-9]+', order)[0]

    if (order_letter == 'N' or order_letter == 'S' or order_letter == 'E' 
                or order_letter == 'W' or order_letter == 'L' or order_letter == 'R'):
        update_waypoint(w_dict, order_letter, order_number)
    else:
        update_ship(s_dict, w_dict, order_number)





def get_file(file_name):
    with open(file_name, 'r') as f:
        list_el_file = [l.rstrip('\n') for l in f]
    return list_el_file



def main():
    movement_orders = get_file('input_test.txt')

    for order in movement_orders:
        print(f'The order is {order}')
        update_the_variables(ship_var, waypoint_var, order)
        print(f'The updated values are for ship {ship_var}, for waypoint {waypoint_var}')

    print(ship_var, waypoint_var)

    manhattan_distance = abs(ship_var['north'] - ship_var['south']) + \
            abs(ship_var['east'] - ship_var['west'])

    print(f'Manhattan distance: {manhattan_distance}')


    return 'ok'



if __name__ == "__main__":
    main()