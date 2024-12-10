from Inputs.puzzle_inputs import puzzle_input_1
from Inputs.test_inputs import test_inputs


def create_map(text: str) -> list[str]:
    return text.strip().split("\n")


def find_starting_positions(t_map: list[str]) -> list[list[int]]:
    starting_positions = []
    for y, row in enumerate(t_map):
        for x, value in enumerate(row):
            if value == "0":
                starting_positions.append((x, y))
    
    return starting_positions


def find_paths(t_map: list[str]) -> tuple[int, int]:
    starting_positions = find_starting_positions(t_map)

    sum_trails = 0
    sum_paths = 0
    for starting_position in starting_positions:
        paths = []
        valid_trails = set()
        valid_paths = []
        movements = [
            [1, 0],
            [-1, 0],
            [0, 1],
            [0, -1]
        ]

        paths.append([starting_position])
        while paths:
            current_path = paths.pop(0)
            cur_x, cur_y = current_path[-1]

            for movement in movements:
                current_path_with_movement = current_path[:]
                new_x = cur_x + movement[0]
                new_y = cur_y + movement[1]

                if new_y < 0 or new_y >= len(t_map):
                    continue
                elif new_x < 0 or new_x >= len(t_map[new_y]):
                    continue
                elif  t_map[new_y][new_x] == ".":
                    continue

                if int(t_map[new_y][new_x]) == int(t_map[cur_y][cur_x]) + 1:
                    current_path_with_movement.append((new_x, new_y))
                    if t_map[new_y][new_x] == "9":
                        valid_trails.add((new_x, new_y))
                        valid_paths.append(current_path_with_movement)
                    else:
                        paths.append(current_path_with_movement[:])
    
        sum_trails += len(valid_trails)
        sum_paths += len(valid_paths)
    
    print(f"There are a total of {sum_trails} valid trail.")
    print(f"There are a total of {sum_paths} valid paths.")
    return sum_trails, sum_paths


test_cases = 0
passed_tests = 0
for key, value in test_inputs.items():
    print(f"Running test {key}.")
    t_map = create_map(value["Input"])
    valid_trails, valid_paths = find_paths(t_map)
    
    tasks = [["Task 1", valid_trails], ["Task 2", valid_paths]]
    for task, answer in tasks:
        if task in value["Answers"]:
            test_cases += 1
            if answer == value["Answers"][task]:
                passed_tests += 1
                print(f"Passed for {task}.")
            else:
                print(f"Failed for {task}.")

    print()

if passed_tests == test_cases:
    print("All tests passes running Puzzle Inputs")
    t_map = create_map(puzzle_input_1)
    valid_trails, valid_paths = find_paths(t_map)
