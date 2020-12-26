

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