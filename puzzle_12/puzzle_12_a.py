import re


def get_file(file_name):
    with open(file_name, 'r') as f:
        list_el_file = [l.rstrip('\n') for l in f]
    return list_el_file







dict_variables = {
    'direction': 'E',
    'degrees': 90,
    'north': 0,
    'south': 0,
    'east': 0,
    'west': 0
}


def get_direction_from_angle(deg):
    if (deg == 0):
        return 'N'
    elif (deg == 90):
        return 'E'
    elif (deg == 180):
        return 'S'
    elif (deg == 270):
        return 'W'


def update_the_variables(var_dict, order):

    # Get letter
    order_letter = re.findall(r'[A-Z]+', order)[0]

    # Get number
    order_number = re.findall(r'[0-9]+', order)[0]

    print(order_letter, order_number)

    if (order_letter == 'F'):
        direction = var_dict['direction']
        if (direction == 'N'):
            var_dict['north'] += int(order_number)
        elif (direction == 'S'):
            var_dict['south'] += int(order_number)
        elif (direction == 'E'):
            var_dict['east'] += int(order_number)
        elif (direction == 'W'):
            var_dict['west'] += int(order_number)
    elif (order_letter == 'N'):
        var_dict['north'] += int(order_number)
    elif (order_letter == 'S'):
        var_dict['south'] += int(order_number)
    elif (order_letter == 'E'):
        var_dict['east'] += int(order_number)
    elif (order_letter == 'W'):
        var_dict['west'] += int(order_number)
    elif (order_letter == 'L' or order_letter == 'R'):
        # turn to left
        print(order_number)
        var_dict['degrees'] = ((var_dict['degrees'] - int(order_number)) % 360 )if order_letter == 'L' else ((var_dict['degrees'] + int(order_number)) % 360)

        var_dict['direction'] = get_direction_from_angle(var_dict['degrees'])



    return var_dict


def main():
    movement_orders = get_file('input.txt')
    print(movement_orders)

    for order in movement_orders:
        update_the_variables(dict_variables, order)

    print(dict_variables)

    manhattan_distance = abs(dict_variables['north'] - dict_variables['south']) + \
                    abs(dict_variables['east'] - dict_variables['west'])

    print(f'Manhattan distance: {manhattan_distance}')

    return 'ok'



if __name__ == "__main__":
    main()
