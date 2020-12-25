

def get_file(file_name):
    with open(file_name, 'r') as f:
        list_el_file = [l.rstrip('\n') for l in f]
    return list_el_file





def main():
    list_adapters = get_file('input.txt')
    list_adapters_int = list(map(int, list_adapters))
    print(list_adapters_int)

    max_built_in_jolts = max(list_adapters_int)
    print(f'The maximum built-in rate of the device is: {max_built_in_jolts}')

    list_adapters_int.sort()
    print(list_adapters_int)

    list_ordered_adapters = []
    list_ordered_adapters.append(0)

    while (True):
        tmp_max_adapter = list_ordered_adapters[-1]
        print(f'Last adapter in the list is: {tmp_max_adapter}')

        # Extraemos los items que sean >= +3 este ultimo item en diferencia
        tmp_list = [i for i in list_adapters_int if i <= tmp_max_adapter+3]
        print(tmp_list)

        # Ordenamos y conectamos todos juntos
        tmp_list.sort()
        
        # Eliminamos estos items de la lista original
        list_ordered_adapters.extend(tmp_list)
        for i in tmp_list:
            list_adapters_int.remove(i)
        print(f'Remaining elements in the original list: {list_adapters_int}')

        # Vemos si sigue habiendo items dentro de esa lista
        if (not list_adapters_int):
            break

    # Añadimos el built-in adapter que es +3 al mayor
    list_ordered_adapters.append(max_built_in_jolts+3)

    print(f'The new ordered list of adapters is: {list_ordered_adapters}')

    # Calculating the differences between each adapter
    list_diff = [list_ordered_adapters[i+1] - list_ordered_adapters[i] for i in range(0, len(list_ordered_adapters)-1)]
    print(f'The list of differences is {list_diff}')

    i = 0
    list_possible_removed_adapters = []
    while (True):
        sum_diff = list_diff[i] + list_diff[i+1]

        if  (sum_diff <=3):
            list_possible_removed_adapters.append(list_ordered_adapters[i+1])

        i += 1

        if (i >= len(list_diff)-1):
            break

    print(list_possible_removed_adapters)
    for i in list_possible_removed_adapters:
        list_ordered_adapters.remove(i)
    print(f'List with all elements removed: {list_ordered_adapters}')
    print(f'The number of possible combinations is {2**len(list_possible_removed_adapters)}')

    return 'ok'



if __name__ == "__main__":
    main()