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

def find_first_largest_number(value):
    movement_order = [[1, 0], [0, -1], [-1, 0], [0, 1]]
    add_values = [[1, 1], [0, 1], [-1, 1], [-1, -1], [0, -1], [1, -1], [1, 0], [-1, 0]]

    position = [0, 0]
    location_values = { 
        0: {
            0:1
        }
    }

    current_value = 0
    current_movement = movement_order.pop(0)
    movement_order.append(current_movement)
    while current_value <= value:
        current_value = 0
        x, y = position
        x += current_movement[0]
        y += current_movement[1]
        position = [x, y]

        if x not in location_values:
            location_values[x] = {}
        if y not in location_values[x]:
            location_values[x][y] = 0
        
        for add_value in add_values:
            check_x = x + add_value[0]
            check_y = y + add_value[1]

            if check_x in location_values and check_y in location_values[check_x]:
                current_value += location_values[check_x][check_y]
            
            location_values[x][y] = current_value
        next_movement = movement_order[0]
        potential_x = x + next_movement[0]
        potential_y = y + next_movement[1]
        if not potential_x in location_values or (potential_x in location_values and not potential_y in location_values[potential_x]):
            current_movement = movement_order.pop(0)
            movement_order.append(current_movement)     
        
    print(f"First largest value is {current_value}")

print("Task 1 distances")
for point in [1, 12, 23, 1024, 325489]:
    print(f"Distance to point {point} is {calculate_distance(point)}.")

print("\nTask 2")
find_first_largest_number(325489)
