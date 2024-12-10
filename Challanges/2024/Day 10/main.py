from Inputs.puzzle_inputs import puzzle_input_1
from Inputs.test_inputs import (
    test_input_1, test_answer_1, 
    test_input_2, test_answer_2,
    test_input_3, test_answer_3,
    test_input_4, test_answer_4,
    test_input_5, test_answer_5
)


def create_map(text: str) -> list[str]:
    return text.strip().split("\n")


def find_starting_positions(t_map: list[str]) -> list[list[int]]:
    starting_positions = []
    for y, row in enumerate(t_map):
        for x, value in enumerate(row):
            if value == "0":
                starting_positions.append((x, y))
    
    return starting_positions


def find_paths(t_map: list[str]) -> None:
    starting_positions = find_starting_positions(t_map)

    sum = 0
    for starting_position in starting_positions:
        paths = []
        valid_paths = set()
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
                        valid_paths.add((new_x, new_y))
                    else:
                        paths.append(current_path_with_movement[:])
    
        print(len(valid_paths))
        sum += len(valid_paths)
    
    print(f"There are a total of {sum} valid paths.")
    return sum

print("Task 1")
test = [[test_input_1, test_answer_1], [test_input_2, test_answer_2], [test_input_3, test_answer_3], [test_input_4, test_answer_4], [test_input_5, test_answer_5]]
test_number = 1
test = [[test_input_5, test_answer_5]]
for test_input, test_answer in test:
    t_map = create_map(test_input)
    valid_paths = find_paths(t_map)

    if valid_paths == test_answer:
        print(f"Correct for test input {test_number}")

    test_number += 1


t_map = create_map(puzzle_input_1)
valid_paths = find_paths(t_map)

if valid_paths == test_answer:
    print(f"Correct for test input {test_number}")