def calculate_distance(access_point):
    if access_point == 1:
        return 0

    length = 1
    current_value = 0
    steps_to_outside = -1

    while current_value < access_point:
        if length == 1:
            current_value = 1
        else:
            current_value += (length * 4) - 4
        length += 2
        steps_to_outside += 1

    length -= 2
    grid = []
    for i in range(length):
        grid.append([None][:] * length)

    populate_current = current_value
    x = length - 1
    y = x
    movement_order = [[-1, 0], [0, -1], [1, 0], [0, 1]]
    current_movement = movement_order.pop(0)
    movement_order.append(current_movement)
    center_position = []
    access_point_position = []
    while populate_current >=1:
        grid[y][x] = populate_current
        if populate_current == access_point:
            access_point_position = [x, y]
        
        x_mov, y_mov = current_movement
        potential_x = x + x_mov
        potential_y = y + y_mov
        if x_mov != 0:
            if potential_x < 0 or potential_x >= length or grid[y][potential_x] != None:
                current_movement = movement_order.pop(0)
                movement_order.append(current_movement)
            else:
                populate_current -= 1
                x = potential_x
        if y_mov != 0:
            if potential_y < 0 or potential_y >= length or grid[potential_y][x] != None:
                current_movement = movement_order.pop(0)
                movement_order.append(current_movement)
            else:
                populate_current -= 1
                y = potential_y
        
        if populate_current == 1:
            grid[y][x] = populate_current
            center_position = [x,y]
            break

    return abs(access_point_position[0] - center_position[0]) + abs(access_point_position[1] - center_position[1])

for point in [1, 12, 23, 1024, 325489]:
    print(f"Distance to point {point} is {calculate_distance(point)}.")
