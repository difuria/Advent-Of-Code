from Inputs.puzzle_inputs import puzzle_input_1
from Inputs.test_inputs import test_answer_1, test_input_1, test_answer_2, test_input_2, test_answer_1_2


def get_grid_and_locations(text: str) -> tuple[list[list[str]], dict[list[str, str]]]:
    text_split = text.strip().split("\n")

    grid = []
    antennas = {} 
    for i, line in enumerate(text_split):
        line_split = list(line)
        grid.append(line_split)
        for j, character in enumerate(line_split):
            if character != ".":
                if character not in antennas:
                    antennas[character] = []
                antennas[character].append([j, i])

    return grid, antennas


def place_antinodes(grid: list[list[str]], antennas: dict[set], task: int = 1) -> None:
    antinode_locations = set()
    for antenna, locations in antennas.items():
        for i in range(len(locations)-1):
            for j in range(i+1, len(locations)):
                x_distance = locations[j][0] - locations[i][0]
                y_distance = locations[j][1] - locations[i][1]

                if task == 1:
                    x_i, y_i = locations[j]
                    x_j, y_j  = locations[i]
                else:
                    # For task 2 set the distance to the furthest direction to count from
                    # so antennas are counted as antinodes
                    x_i, y_i = locations[i]
                    x_j, y_j = locations[j]        

                # Keep looping while we inside the grid
                while (y_i >= 0 and y_i < len(grid) and x_i >= 0 and x_i < len(grid[y_i])) or \
                     (y_j >= 0 and y_j < len(grid) and x_j >= 0 and x_j < len(grid[y_j])):
                    if x_distance < 0:
                        x_i -= abs(x_distance)
                        x_j += abs(x_distance)
                    else:
                        x_i += abs(x_distance)
                        x_j -= abs(x_distance)

                    if y_distance < 0:
                        y_i -= abs(y_distance)
                        y_j += abs(y_distance)
                    else:
                        y_i += abs(y_distance)
                        y_j -= abs(y_distance)

                    if y_i >= 0 and y_i < len(grid) and x_i >= 0 and x_i < len(grid[y_i]):
                        grid[y_i][x_i] = "#"
                        antinode_locations.add((x_i, y_i))
                    
                    if y_j >= 0 and y_j < len(grid) and x_j >= 0 and x_j < len(grid[y_j]):
                        grid[y_j][x_j] = "#"
                        antinode_locations.add((x_j, y_j))
                    
                    if task == 1:
                        break

    print(f"There are {len(antinode_locations)} antinode locations.")
    return antinode_locations


print("Task 1")
print("Test Input")
grid, antennas = get_grid_and_locations(test_input_1)
antinode_locations = place_antinodes(grid, antennas)

if len(antinode_locations) == test_answer_1:
    print("Puzzle Input")
    grid, antennas = get_grid_and_locations(puzzle_input_1)
    antinode_locations = place_antinodes(grid, antennas)

print("\nTask 2")
print("Test Input")
grid, antennas = get_grid_and_locations(test_input_2)
antinode_locations = place_antinodes(grid, antennas, 2)

if len(antinode_locations) == test_answer_2:
    print("Puzzle Input")
    grid, antennas = get_grid_and_locations(puzzle_input_1)
    antinode_locations = place_antinodes(grid, antennas, 2)