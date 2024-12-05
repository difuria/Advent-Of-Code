from Inputs.puzzle_inputs import puzzle_input_1
from Inputs.test_inputs import test_inputs_1


def build_grid(x: int = 1000, y: int = 1000) -> list:
    grid = []
    for i in range(x):
        grid.append([0][:] * y)
    
    return grid


def build_instructions(text: str) -> list:
    split_text = text.strip().split("\n")

    instructions = []
    for line in split_text:
        line = line.strip().split(" ")
        if line[0] == "toggle":
            indexes = [1, 3]
        else:
            indexes = [2, 4]

        for index in indexes:
            line[index] = list(map(int, line[index].split(",")))

        instructions.append(line)

    return instructions


def follow_instructions_lighting(grid: list, instructions: list) -> list:
    for instruction in instructions:
        if instruction[0] == "turn":
            state = 1 if instruction[1] == "on" else 0

            start_x, start_y = instruction[2]
            end_x, end_y = instruction[4]

            for y in range(start_y, end_y+1):
                for x in range(start_x, end_x+1):
                    grid[y][x] = state
        else:
            start_x, start_y = instruction[1]
            end_x, end_y = instruction[3]            

            for y in range(start_y, end_y+1):
                for x in range(start_x, end_x+1):
                    grid[y][x] = 1 if grid[y][x] == 0 else 0
    
    return grid


def follow_brightness_instructions(grid: list, instructions: list) -> list:
    for instruction in instructions:
        if instruction[0] == "turn":
            state = 1 if instruction[1] == "on" else -1

            start_x, start_y = instruction[2]
            end_x, end_y = instruction[4]

            for y in range(start_y, end_y+1):
                for x in range(start_x, end_x+1):
                    grid[y][x] += state

                    if grid[y][x] < 0:
                        grid[y][x] = 0
        else:
            start_x, start_y = instruction[1]
            end_x, end_y = instruction[3]            

            for y in range(start_y, end_y+1):
                for x in range(start_x, end_x+1):
                    grid[y][x] += 2
    
    return grid


def count_lights(grid: list) -> None:
    count = 0
    for row in grid:
        for light in row:
            if light == 1:
                count += 1
    
    print(f"There are {count} lights lit up.")


def get_brightness(grid: list) -> None:
    brightness = 0
    for row in grid:
        for light in row:
            brightness += light
    
    print(f"The lights are {brightness} bright.")


grid = build_grid()
instructions = build_instructions(puzzle_input_1)
lit_grid = follow_instructions_lighting(grid, instructions)
count_lights(lit_grid)

grid = build_grid()
brightness_grid = follow_brightness_instructions(grid, instructions)
get_brightness(brightness_grid)
