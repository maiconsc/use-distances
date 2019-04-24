def compute_node_distance(grid, xcoord, ycoord, last_d, max_d):

    if last_d == max_d:
        return None

    if is_up(xcoord) and is_right(ycoord):
        if grid[ycoord - 1][xcoord] >= last_d:
            grid[ycoord - 1][xcoord] = last_d + 1
        compute_node_distance(grid, xcoord, ycoord - 1, last_d + 1, max_d)
        if grid[ycoord][xcoord + 1] >= last_d:
            grid[ycoord][xcoord + 1] = last_d + 1
        compute_node_distance(grid, xcoord + 1, ycoord, last_d + 1, max_d)

    elif is_up(xcoord) and is_left(ycoord):
        if grid[ycoord - 1][xcoord] >= last_d:
            grid[ycoord - 1][xcoord] = last_d + 1
        compute_node_distance(grid, xcoord, ycoord - 1, last_d + 1, max_d)
        if grid[ycoord][xcoord - 1] >= last_d:
            grid[ycoord][xcoord - 1] = last_d + 1
        compute_node_distance(grid, xcoord - 1, ycoord, last_d + 1, max_d)

    elif is_down(xcoord) and is_right(ycoord):
        if grid[ycoord + 1][xcoord] >= last_d:
            grid[ycoord + 1][xcoord] = last_d + 1
        compute_node_distance(grid, xcoord, ycoord + 1, last_d + 1, max_d)
        if grid[ycoord][xcoord + 1] >= last_d:
            grid[ycoord][xcoord + 1] = last_d + 1
        compute_node_distance(grid, xcoord + 1, ycoord, last_d + 1, max_d)

    elif is_down(xcoord) and is_left(ycoord):
        if grid[ycoord + 1][xcoord] >= last_d:
            grid[ycoord + 1][xcoord] = last_d + 1
        compute_node_distance(grid, xcoord, ycoord + 1, last_d + 1, max_d)
        if grid[ycoord][xcoord - 1] >= last_d:
            grid[ycoord][xcoord - 1] = last_d + 1
        compute_node_distance(grid, xcoord - 1, ycoord, last_d + 1, max_d)


def is_up(xcoord):
    result = False
    if xcoord % 2 == 0:
        result = True
    return result


def is_down(xcoord):
    result = False
    if xcoord % 2 != 0:
        result = True
    return result


def is_right(ycoord):
    result = False
    if ycoord % 2 == 0:
        result = True
    return result


def is_left(ycoord):
    result = False
    if ycoord % 2 != 0:
        result = True
    return result


def print_grid(grid):

    grid_printer = ''
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if grid[i][j] == 999:
                grid[i][j] = '--'
            grid_printer += ' ' + str(grid[i][j]).zfill(2)
        grid_printer += '\n'
    grid_printer = grid_printer[1::1].replace('\n ', '\n')
    print(grid_printer)


def create_empty_grid(size):

    grid = list(list())
    for i in range(0, size):
        line_aux = list()
        for j in range(0, size):
            line_aux.append(999)
        grid.append(line_aux)
    return grid


def define_starting_point(x0, y0, grid):
    grid[y0][x0] = 0
    return grid


def create_instance(x0, y0, max_d, size):

    grid = create_empty_grid(size)
    grid = define_starting_point(x0, y0, grid)
    print('Computing...')
    compute_node_distance(grid, x0, y0, 0, max_d)
    return grid


def distance_matrix_to_list(grid):
    list


if __name__ == '__main__':

    size = 60
    max_d = 25

    # 1
    x0 = int(size/2)
    y0 = int(size/2)
    grid_1 = create_instance(x0, y0, max_d, size)
    print_grid(grid_1)

    # 2
    x0 = int(size/2) + 1
    y0 = int(size/2)
    grid_2 = create_instance(x0, y0, max_d, size)
    print_grid(grid_2)

    # 3
    x0 = int(size/2)
    y0 = int(size/2) + 1
    grid_3 = create_instance(x0, y0, max_d, size)
    print_grid(grid_3)

    # 4
    x0 = int(size/2) + 1
    y0 = int(size/2) + 1
    grid_4 = create_instance(x0, y0, max_d, size)
    print_grid(grid_4)
