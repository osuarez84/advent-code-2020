






def get_file(file_name):
    with open(file_name, 'r') as f:
        list_el_file = [l.rstrip('\n') for l in f]
    return list_el_file





def main():    
    list_bags_raw = get_file('input.txt')


    return 0



if __name__ == "__main__":
    main()