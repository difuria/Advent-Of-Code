from Inputs.puzzle_inputs import puzzle_input_1
from Inputs.test_inputs import test_input_1


def get_grid(text: str) -> None:
    text_split = text.strip().split("\n")

    grid = []
    for row in text_split:
        grid.append(list(row))
    
    return grid


def find_starting_position(grid: list) -> list:
    for y, row in enumerate(grid):
        for x in range(len(row)):
            if grid[y][x] == "^":
                return [x, y]
    
    raise ValueError(f"Undefined starting position")


def print_grid(grid: list) -> None:
    for row in grid:
        print("".join(row))


def find_movement(grid: list, position: list) -> list:
    in_grid = True

    movements = [
        [0, -1],
        [1, 0],
        [0, 1],
        [-1, 0]
    ]

    x, y = position
    grid[y][x] = "X"
    current_movement = movements.pop(0)
    while in_grid:
        new_x = x + current_movement[0]
        new_y = y + current_movement[1]

        if new_y < 0 or new_y >= len(grid):
            in_grid = False
        elif new_x < 0 or new_x >= len(grid[new_y]):
            in_grid = False
        elif grid[new_y][new_x] == "#":
            movements.append(current_movement)
            current_movement = movements.pop(0)
            print_grid(grid)
        else:
            grid[new_y][new_x] = "X"
            x = new_x
            y = new_y
    
    movement_count = 0
    for row in grid:
        for column in row:
            if column == "X":
                movement_count += 1

    print(f"A total of {movement_count} was visited.")
    return grid


grid = get_grid(puzzle_input_1)
starting_position = find_starting_position(grid)
movement_grid = find_movement(grid, starting_position)