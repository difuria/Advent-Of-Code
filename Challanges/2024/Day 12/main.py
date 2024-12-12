from Inputs.puzzle_inputs import puzzle_input_1
from Inputs.test_inputs import test_inputs

def get_unique_sides(perimeter: list[tuple[int]]) -> int:
    """
    Direction is used so that a top and bottom boundary which are
    touching don't cancel each other out. Such as:
    .XXX..
    .X.X..
    .X..X.
    .XXXX.
    """
    starting_positions = []

    while perimeter:
        current_start = perimeter.pop(0)
        starting_positions.append(current_start)

        left_x, left_y, direction = current_start
        right_x, right_y, direction = current_start
        up_x, up_y, direction = current_start
        down_x, down_y, direction = current_start

        while True:
            left_x -= 1

            left_search = (left_x, left_y, direction)
            if left_search in perimeter:
                perimeter.remove(left_search)
            else:
                break

        while True:
            right_x += 1

            right_search = (right_x, right_y, direction)
            if right_search in perimeter:
                perimeter.remove(right_search)
            else:
                break
        
        while True:
            up_y -= 1

            up_search = (up_x, up_y, direction)
            if up_search in perimeter:
                perimeter.remove(up_search)
            else:
                break

        while True:
            down_y += 1

            down_search = (down_x, down_y, direction)
            if down_search in perimeter:
                perimeter.remove(down_search)
            else:
                break

    return len(starting_positions)


def search_area(start: tuple[int], grid: list[list[str]], seen: set[tuple[int]]) -> tuple[set[tuple[int]], int]:
    perimeter = []
    area = 1
    char = grid[start[1]][start[0]]
    seen.add((start[0], start[1]))
    movements = [
        (1, 0, "R"),
        (-1, 0, "L"),
        (0, 1, "U"),
        (0, -1, "D")
    ]

    queue = [start]
    while queue:
        x, y = queue.pop(0)

        for movement in movements:
            new_x = x + movement[0]
            new_y = y + movement[1]
            new_pos = (new_x, new_y)
            par_pos = (new_x, new_y, movement[2])

            if new_y < 0 or new_y >= len(grid):
                perimeter.append(par_pos)
                continue
            elif new_x < 0 or new_x >= len(grid[new_y]):
                perimeter.append(par_pos)
                continue
            elif grid[new_y][new_x] != char:
                perimeter.append(par_pos)
            elif new_pos in seen:
                continue
            else:
                area += 1
                seen.add(new_pos)
                queue.append(new_pos)

    cost = len(perimeter) * area

    sides = get_unique_sides(perimeter)
    bulk_cost = sides * area
    return seen, cost, bulk_cost


def search_grid(text: str):
    grid = [list(line) for line in text.strip().split("\n")]

    # Store each coordinate that we've seen so we don't return
    seen = set()
    cost = 0
    bulk_cost = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            position = (x, y)
            if position in seen:
                continue

            seen, current_cost, current_bulk_cost = search_area(position, grid, seen)
            cost += current_cost
            bulk_cost += current_bulk_cost

    print(f"Cost of fencing for this grid is {cost}.")
    print(f"Bulk cost of fencing for this grid is {bulk_cost}.")
    return cost, bulk_cost


tests = 0
passed = 0
for test_id, contents in test_inputs.items():
    if "Task 1" in contents["Answer"]:
        tests += 1
    if "Task 2" in contents["Answer"]:
        tests+= 1
    
    print(f"Running test {test_id}.")
    cost, bulk_cost = search_grid(contents["Input"])
    if "Task 1" in contents["Answer"]:
        if cost == contents["Answer"]["Task 1"]:
            passed += 1
            print("Passed for Task 1")
        else:
            print("Failed for Task 1")

    if "Task 2" in contents["Answer"]:
        if bulk_cost == contents["Answer"]["Task 2"]:
            passed += 1
            print("Passed for Task 2")
        else:
            print("Failed for Task 2")
    
    print()

if tests == passed:
    print("\nAll tests passed running puzzle input")
    search_grid(puzzle_input_1)
