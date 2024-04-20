import os, sys

def get_file(path, file):
    file = os.path.join(path, f"Task Inputs", file)

    if not os.path.exists(file):
        print(f"Invalid file supplied of {file}")
        sys.exit(1)

    with open(file, "r") as f:
        path_info = f.read()

    return path_info

def ensure_all_grid_rows_match(grid:list):
    longest_row = 0
    for row in grid:
        longest_row = max(longest_row, len(row))
    

    for i, row in enumerate(grid):
        if len(row) < longest_row:
            difference = longest_row - len(row)
            additional = [""] * (difference // 2)
            grid[i] = additional[:] + grid[i] + additional[:]

    return grid

def location(directions:str, grid:list, current_location:list=[1,1]):
    grid = ensure_all_grid_rows_match(grid)

    movements = {
        "U": [0, -1],
        "D": [0, 1],
        "R": [1, 0],
        "L": [-1, 0]
    }

    for direction in directions:
        movement = movements[direction]
        current_location[0] += movement[0]
        current_location[1] += movement[1]

        if current_location[1] < 0:
            current_location[1] = 0
        elif current_location[1] >= len(grid):
            current_location[1] = len(grid) - 1

        y = current_location[1]
        if current_location[0] < 0:
            current_location[0] = 0
        elif current_location[0] >= len(grid[y]):
            current_location[0] = len(grid[y]) - 1

        x, y = current_location
        if grid[y][x] == "":
            current_location[0] -= movement[0]
            current_location[1] -= movement[1]
    x, y = current_location
    return grid[y][x], current_location

def get_code(direction_list:str, grid:list, current_location:list=[1, 1]):
    code = ""
    for directions in direction_list.strip().splitlines():
        current_digit, current_location = location(directions, grid, current_location)
        code += str(current_digit)
    
    print(f"Code is {code}.")

if __name__ == "__main__":
    path = os.path.dirname(__file__)

    print("Task 1")
    grid = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    get_code(get_file(path, "test_instructions_1.txt"), grid)
    get_code(get_file(path, "puzzle_instructions_1.txt"), grid)

    print("Task 2")
    grid = [
                  ["1"],
             ["2", "3", "4"],
        ["5", "6", "7", "8", "9"],
             ["A", "B", "C"],
                  ["D"]
    ]
    get_code(get_file(path, "test_instructions_1.txt"), grid, [0, 2])
    get_code(get_file(path, "puzzle_instructions_1.txt"), grid, [0, 2])