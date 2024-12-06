from Inputs.puzzle_inputs import puzzle_input_1
from Inputs.test_inputs import test_input_1

from typing import List, Tuple


def get_grid(text: str) -> None:
    text_split: list = text.strip().split("\n")

    grid: list = []
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


def find_movement(grid: list, position: list, o_position: tuple = ()) -> Tuple[List[int], Tuple[int, int], List[int]]:
    in_grid: bool = True
    o_positions: list = []

    if o_position:
        grid[o_position[1]][o_position[0]] = "O"

    movements = [
        (0, -1),
        (1, 0),
        (0, 1),
        (-1, 0)
    ]

    x, y = position
    grid[y][x] = "X"
    o_positions.append((x, y))
    current_movement = movements.pop(0)

    # Hash can be used to determing if a path has been used before
    repeating_locations: dict = {
        (x,y): {current_movement}
    }

    while in_grid:
        new_x = x + current_movement[0]
        new_y = y + current_movement[1]

        if new_y < 0 or new_y >= len(grid) or new_x < 0 or new_x >= len(grid[new_y]):
            in_grid = False
        elif grid[new_y][new_x] in ["#", "O"]:
            movements.append(current_movement)
            current_movement = movements.pop(0)
        else:
            grid[new_y][new_x] = "X"
            x = new_x
            y = new_y

            current_position = (x, y)
            """
            We know for the guard to bump into the obstacle they have to have walked over it previously.
            Meaning we can use the X map to get a list of possible positions to reduce trying every space
            in the grid.
            """
            o_positions.append(current_position)
            if current_position not in repeating_locations:
                repeating_locations[current_position] = set()
            elif current_movement in repeating_locations[current_position]:
                return grid, o_position, o_positions

            repeating_locations[current_position].add(current_movement)

    movement_count: int = 0
    for row in grid:
        movement_count += row.count("X")

    if not o_position:
        print(f"A total of {movement_count} was visited.")

    return grid, (), o_positions


current_input = puzzle_input_1
print("Task 1")
grid = get_grid(current_input)
starting_position = find_starting_position(grid)
movement_grid, repeating_position, o_positions = find_movement(grid, starting_position)

# Solution for task 2:
# track where the guard has been and what direction they were travelling when there. Then if ever revisited in the same direction we know we've found a loop
# On the original track make a list of grid positions to place an O and cycle through the list. 
# repeating_locations = {
#     (x,y): set(direction -> (1, 0))
# }
print("Task 2")
possible_repeating_positions = set()
for o_position in o_positions:
    grid = get_grid(current_input)
    grid, repeating_position, o_positions = find_movement(grid, starting_position, o_position)

    if repeating_position:
        possible_repeating_positions.add(repeating_position)

print(f"There are a total of {len(possible_repeating_positions)} repeating obstacle positions.")