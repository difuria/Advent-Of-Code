from Inputs.puzzle_inputs import puzzle_inputs_1
from Inputs.test_inputs import test_input_1, test_input_2

import re


def find_robots(text: str) -> list[dict[str, list[int]]]:
    robots = []
    coordinates = re.findall(r"p=(\d{1,}),(\d{1,})\s{1,}v=((-|)\d{1,}),((-|)\d{1,})", text)

    for coordinate in coordinates:
        robot = {
            "pos": [int(coordinate[0]), int(coordinate[1])],
            "mov": [int(coordinate[2]), int(coordinate[4])]
        }
        robots.append(robot)

    return robots


def move_robots(robots: list[dict[str, list[int]]], seconds: int, grid_size: list[int] = [101, 103]) -> tuple[list[dict[str, list[int]]], set[tuple[int]]]:
    robot_positions = set()
    for i, robot in enumerate(robots):
        x_mov = robot["mov"][0] * seconds
        y_mov = robot["mov"][1] * seconds

        new_x_pos = robot["pos"][0] + x_mov
        new_y_pos = robot["pos"][1] + y_mov

        # Place the robot back inside the grid
        x_grids = new_x_pos // grid_size[0]
        new_x_pos = new_x_pos - (x_grids * grid_size[0])

        y_grids = new_y_pos // grid_size[1]
        new_y_pos = new_y_pos - (y_grids * grid_size[1])

        robot["pos"] = [new_x_pos, new_y_pos]
        robots[i] = robot

        robot_positions.add((new_x_pos, new_y_pos))
    
    return robots, robot_positions


def calculate_robots_in_quadrants(robots: list[dict[str, list[int]]], grid_size: list[int] = [101, 103]):
    mid_x = (grid_size[0] // 2)
    mid_y = (grid_size[1] // 2)
    print(mid_x, mid_y)
    # Top Left, Top Right, Bottom Left, Bottom Right
    quadrant_count = [0, 0, 0, 0]

    for robot in robots:
        rob_x, rob_y = robot["pos"]
        # Top half
        if rob_y < mid_y:
            if rob_x < mid_x:
                quadrant_count[0] += 1
            elif rob_x > mid_x:
                quadrant_count[1] += 1
        elif rob_y > mid_y:
            if rob_x < mid_x:
                quadrant_count[2] += 1
            elif rob_x > mid_x:
                quadrant_count[3] += 1

    print(quadrant_count)  

    safety_count = 0
    for quadrant in quadrant_count:
        if quadrant_count == 0:
            continue
        elif safety_count == 0:
            safety_count = 1
        
        safety_count *= quadrant

    print(f"Safety count is {safety_count}")     


def find_tree(robots: list[dict[str, list[int]]]) -> None:
    """
    There is probably a better way of solving task 2. For this solution we're just finding the first time 
    20 robots are surrounded by other robots. Then assuming that must be the tree.
    """
    i = 1
    while True:
        robots, robot_positions = move_robots(robots, 1)
        count = 0
        for robot in robots:
            x, y = robot["pos"]
            # Lets just see if we can find something surrounded
            mov_count = 0
            movements = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for movement in movements:
                new_x = movement[0] + x
                new_y = movement[1] + y

                if (new_x, new_y) not in robot_positions:
                    break

                mov_count += 1

            if mov_count == 4:
                count += 1
        
        if count >= 20:
            print_grid(robots)
            print(f"{i} steps were taken before the tree was seen.")
            break
        i += 1


def print_grid(robots: list[dict[str, list[int]]], grid_size: list[int] = [101, 103]) -> list[list[str, int]]:
    grid = []
    for i in range(grid_size[1]):
        grid.append([])
        for j in range(grid_size[0]):
            grid[i].append(".")
    
    for robot in robots:
        x, y = robot["pos"]
        
        if grid[y][x] == ".":
            grid[y][x] = 0

        grid[y][x] += 1

    for line in grid:
        print_line = ""
        for char in line:
            print_line += str(char)

        print(print_line)


print("Test Inputs")
grid_size = [11, 7]
robots = find_robots(test_input_1)
robots, robot_positions = move_robots(robots, 5, grid_size)
print_grid(robots, grid_size)
calculate_robots_in_quadrants(robots, grid_size)

print()
robots = find_robots(test_input_2)
robots, robot_positions = move_robots(robots, 100, grid_size)
print_grid(robots, grid_size)
calculate_robots_in_quadrants(robots, grid_size)

print()
print("Puzzle Input")
print("Task 1")
robots = find_robots(puzzle_inputs_1)
robots, robot_positions = move_robots(robots, 100)
print_grid(robots)
calculate_robots_in_quadrants(robots)

print("\nTask 2")
robots = find_robots(puzzle_inputs_1)
find_tree(robots)