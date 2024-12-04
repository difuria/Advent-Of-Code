from Inputs.puzzle_inputs import puzzle_input_1
from Inputs.test_inputs import test_input_1


def breadth_first_search(text: list, desired_word: str, i: int, j: int) -> list:
    queue = []
    current_path = [[i, j]]
    for x in range(-1, 2, 1):
        for y in range(-1, 2, 1):
            if x == 0 and y == 0:
                # Wouldn't be moving
                continue

            new_x = i + x
            new_y = j + y

            if new_y >= len(text) or new_y < 0:
                continue
            elif new_x >= len(text[new_y]) or new_x < 0:
                continue
            elif desired_word[1] == text[new_y][new_x]:
                # current position
                # moving position
                # current index
                # Current path for debugging
                queue.append([
                    [new_x, new_y],
                    [x, y],
                    1,
                    current_path + [[new_x, new_y]]
                ])

    found = []
    while queue: 
        current_position, movement, current_index, current_path = queue.pop()

        new_x = current_position[0] + movement[0]
        new_y = current_position[1] + movement[1]
        if new_y >= len(text) or new_y < 0:
            continue
        elif new_x >= len(text[new_y]) or new_x < 0:
            continue

        current_index += 1
        if text[new_y][new_x] == desired_word[current_index]:
            current_path.append([new_x, new_y])
            
            if current_index == len(desired_word) - 1:
                found.append(current_path)
            else:
                queue.append([
                    [new_x, new_y],
                    movement,
                    current_index,
                    current_path
                ])

    return found


def find_starting_letter(text: list, desired_word="XMAS") -> list:
    found = []
    for y, line in enumerate(text):
        for x, letter in enumerate(line):
            if letter != desired_word[0]:
                continue

            current_find = breadth_first_search(text, desired_word, x, y)
            if current_find:
                found += current_find
    
    print(f"Found {len(found)} {desired_word}")

    return found


def print_map(found: list, text:str) -> None:
    # To view visual representation of output
    arr = []
    for i in range(len(text)):
        arr.append([])
        for j in range(len(text[i])):
            arr[-1].append(".")

    for f in found:
        for x, y in f:
            arr[y][x] = text[y][x]

    new_text = ""
    for line in arr:
        new_text += "".join(line) + "\n"

    print(new_text)


def corner_in_text(text:str, corners: list) -> bool:
    for corner in corners:
        x, y = corner

        if y >= len(text) or y < 0:
            return False
        elif x >= len(text[y]) or x < 0:
            return False

    return True


def x_mas_map(text: list) -> list:
    found = []
    for y, line in enumerate(text):
        for x, letter in enumerate(line):
            if letter == "A":
                find = [["M", "S"], ["M", "S"]]
                top_left_corner = [x - 1, y + 1]
                bottom_left_corner = [x - 1, y -1]
                top_right_corner = [x + 1, y + 1]
                bottom_right_corner = [x + 1, y - 1]

                if not corner_in_text(text, [top_left_corner, bottom_left_corner, top_right_corner, bottom_right_corner]):
                    continue

                t_l_x, t_l_y = top_left_corner
                b_l_x, b_l_y = bottom_left_corner
                t_r_x, t_r_y = top_right_corner
                b_r_x, b_r_y = bottom_right_corner

                if text[t_l_y][t_l_x] in find[0]:
                    find[0].remove(text[t_l_y][t_l_x])
                    if text[b_r_y][b_r_x] != find[0][0]:
                        continue
                else:
                    continue

                if text[t_r_y][t_r_x] in find[1]:
                    find[1].remove(text[t_r_y][t_r_x])
                    if text[b_l_y][b_l_x] != find[1][0]:
                        continue
                else:
                    continue

                found.append([[x, y], top_left_corner, bottom_right_corner, top_right_corner, bottom_left_corner])
    
    print(f"We've found {len(found)} X-MASes")
    return found


test_text = test_input_1.split("\n")
puzzle_text = puzzle_input_1.split("\n")

print("Task 1")
task_1_test_found = find_starting_letter(test_text)
print_map(task_1_test_found, test_text)
task_1_puzzle_found = find_starting_letter(puzzle_text)


print("\nTask 2")
found = x_mas_map(test_text)
print_map(found, test_text)
x_mas_map(puzzle_text)
