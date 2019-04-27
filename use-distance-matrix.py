def compute_node_distance(grid, xcoord, ycoord, last_d, max_d):
    '''
    Recursive method for computing node distance.
    :param grid: USE grid.
    :param xcoord: x-axis coordinate.
    :param ycoord: y-axis coordinate.
    :param last_d: last distance computed.
    :param max_d: max distance to be computed.
    :return: a modified grid with the distance (x, y) to the origin computed.
    '''

    if last_d == max_d:
        return None

    if is_up(xcoord) and is_right(ycoord):
        if grid[ycoord - 1][xcoord] >= last_d:
            grid[ycoord - 1][xcoord] = last_d + 1
        else:
            return None
        compute_node_distance(grid, xcoord, ycoord - 1, last_d + 1, max_d)
        if grid[ycoord][xcoord + 1] >= last_d:
            grid[ycoord][xcoord + 1] = last_d + 1
        else:
            return None
        compute_node_distance(grid, xcoord + 1, ycoord, last_d + 1, max_d)

    elif is_up(xcoord) and is_left(ycoord):
        if grid[ycoord - 1][xcoord] >= last_d:
            grid[ycoord - 1][xcoord] = last_d + 1
        else:
            return None
        compute_node_distance(grid, xcoord, ycoord - 1, last_d + 1, max_d)
        if grid[ycoord][xcoord - 1] >= last_d:
            grid[ycoord][xcoord - 1] = last_d + 1
        else:
            return None
        compute_node_distance(grid, xcoord - 1, ycoord, last_d + 1, max_d)

    elif is_down(xcoord) and is_right(ycoord):
        if grid[ycoord + 1][xcoord] >= last_d:
            grid[ycoord + 1][xcoord] = last_d + 1
        else:
            return None
        compute_node_distance(grid, xcoord, ycoord + 1, last_d + 1, max_d)
        if grid[ycoord][xcoord + 1] >= last_d:
            grid[ycoord][xcoord + 1] = last_d + 1
        else:
            return None
        compute_node_distance(grid, xcoord + 1, ycoord, last_d + 1, max_d)

    elif is_down(xcoord) and is_left(ycoord):
        if grid[ycoord + 1][xcoord] >= last_d:
            grid[ycoord + 1][xcoord] = last_d + 1
        else:
            return None
        compute_node_distance(grid, xcoord, ycoord + 1, last_d + 1, max_d)
        if grid[ycoord][xcoord - 1] >= last_d:
            grid[ycoord][xcoord - 1] = last_d + 1
        else:
            return None
        compute_node_distance(grid, xcoord - 1, ycoord, last_d + 1, max_d)


def is_up(xcoord):
    '''
    Test if the x-axis coordinate correspond to an up column.
    :param xcoord: x-axis coordinate.
    :return: True for an up column and False otherwise.
    '''

    result = False
    if xcoord % 2 == 0:
        result = True
    return result


def is_down(xcoord):
    '''
    Test if the x-axis coordinate correspond to a down column.
    :param xcoord: x-axis coordinate.
    :return: True for a down column and False otherwise.
    '''

    result = False
    if xcoord % 2 != 0:
        result = True
    return result


def is_right(ycoord):
    '''
    Test if the y-axis coordinate correspond to a right row.
    :param xcoord: y-axis coordinate.
    :return: True for a right row and False otherwise.
    '''

    result = False
    if ycoord % 2 == 0:
        result = True
    return result


def is_left(ycoord):
    '''
    Test if the y-axis coordinate correspond to a left row.
    :param xcoord: y-axis coordinate.
    :return: True for a left row and False otherwise.
    '''

    result = False
    if ycoord % 2 != 0:
        result = True
    return result


def print_grid(grid):
    '''
    Print the grid into the screen.
    :param grid: USE grid.
    :return: void.
    '''

    grid_printer = ''
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            grid_printer += ' ' + str(grid[i][j]).zfill(2)
        grid_printer += '\n'
    grid_printer = grid_printer[1::1].replace('\n ', '\n')
    print(grid_printer)


def create_empty_grid(size):
    '''
    Create an empty USE grid (containing 999 in every position).
    :param size: size of the USE grid.
    :return: a grid containing 999 in every position.
    '''

    grid = list(list())
    for i in range(0, size):
        line_aux = list()
        for j in range(0, size):
            line_aux.append(999)
        grid.append(line_aux)
    return grid


def define_starting_point(x0, y0, grid):
    '''
    Define the starting point into the USE grid.
    :param x0: x-axis coordinate of the origin.
    :param y0: y-axis coordinate of the origin.
    :param grid: USE grid.
    :return: USE grid with the origin containing 0.
    '''

    grid[y0][x0] = 0
    return grid


def normalize_grid(grid):
    '''
    Replace each 999 from the grid (used in the recursive step) for the string '--'.
    :param grid: USE grid.
    :return: a modified grid.
    '''

    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if grid[i][j] == 999:
                grid[i][j] = '--'
    return grid


def create_instance(x0, y0, max_d, size):
    '''
    Create an instance for computing the distances in the USE grid.
    :param x0: x-axis coordinate of the origin.
    :param y0: y-axis coordinate of the origin.
    :param max_d: the max distance to be calculated.
    :param size: the size of the USE grid.
    :return: an USE grid with distances computed.
    '''

    grid = create_empty_grid(size)
    grid = define_starting_point(x0, y0, grid)
    compute_node_distance(grid, x0, y0, 0, max_d)
    return normalize_grid(grid)


def distance_matrix_to_list(grid, x0, y0, max_d):
    '''
    Create a list of distances from the matrix.
    :param grid: USE grid.
    :param x0: x-axis coordinate of the origin.
    :param y0: y-axis coordinate of the origin.
    :param max_d: max USE distance computed from the origin.
    :return: a list wih the distances computed. each line 'i' represents the coordinates which has an 'i' USE distance
             to the origin.
    '''

    list_distances = list(list())

    for i in range(0, max_d+2):
        list_distances.append([])
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if grid[i][j] != '--':
                coord = [j-x0, i-y0]
                list_distances[int(grid[i][j])].append(coord)
    if is_up(x0) and is_right(y0):
        list_distances[len(list_distances)-1].append('up-right')
    elif is_up(x0) and is_left(y0):
        list_distances[len(list_distances) - 1].append('up-left')
    elif is_down(x0) and is_right(y0):
        list_distances[len(list_distances)-1].append('down-right')
    elif is_down(x0) and is_left(y0):
        list_distances[len(list_distances) - 1].append('down-left')
    return list_distances


def write_file_distances(filename, distance_list):
    '''
    Write a .txt file with the results of the computation (list of distances).
    :param filename: the name of the file.
    :param distance_list: distance list to be written in the .txt file.
    :return: void.
    '''

    filename = filename.replace('[\'', '').replace('\']', '')
    f = open(f'results/{filename}', 'w+')
    string = ''.join(str(e) for e in distance_list)
    f.write(string.replace(']][', ']]\n['))
    f.close()
    print(f'File {filename} successfully written!')


if __name__ == '__main__':

    # input data here:
    size = 60
    max_d = 25

    # 1st possible coordinate of the origin
    x0 = int(size/2)
    y0 = int(size/2)
    print('Computing...')
    grid_1 = create_instance(x0, y0, max_d, size)
    print_grid(grid_1)
    distance_list1 = distance_matrix_to_list(grid_1, x0, y0, max_d)
    print(distance_list1)
    write_file_distances(f'{distance_list1[len(distance_list1)-1]}_{max_d}.txt', distance_list1)

    # 2nd possible coordinate of the origin
    x0 = int(size/2) + 1
    y0 = int(size/2)
    print('Computing...')
    grid_2 = create_instance(x0, y0, max_d, size)
    print_grid(grid_2)
    distance_list2 = distance_matrix_to_list(grid_2, x0, y0, max_d)
    print(distance_list2)
    write_file_distances(f'{distance_list2[len(distance_list2)-1]}_{max_d}.txt', distance_list2)

    # 3rd possible coordinate of the origin
    x0 = int(size/2)
    y0 = int(size/2) + 1
    print('Computing...')
    grid_3 = create_instance(x0, y0, max_d, size)
    print_grid(grid_3)
    distance_list3 = distance_matrix_to_list(grid_3, x0, y0, max_d)
    print(distance_list3)
    write_file_distances(f'{distance_list3[len(distance_list3)-1]}_{max_d}.txt', distance_list3)

    # 4th possible coordinate of the origin
    x0 = int(size/2) + 1
    y0 = int(size/2) + 1
    print('Computing...')
    grid_4 = create_instance(x0, y0, max_d, size)
    print_grid(grid_4)
    distance_list4 = distance_matrix_to_list(grid_4, x0, y0, max_d)
    print(distance_list4)
    write_file_distances(f'{distance_list4[len(distance_list4)-1]}_{max_d}.txt', distance_list4)
