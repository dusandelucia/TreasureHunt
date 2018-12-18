def read():
    print('Insert values (5 integeres per line separated by space):')
    treasure_map = []

    for i in range(5):
        line = input()
        line_list = []
        for num in line.split(' '):
            line_list.append(int(num))
        treasure_map.append(line_list)

    return treasure_map
