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
    # to view comparison
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


text = test_input_1.split("\n")
found = find_starting_letter(text)
print_map(found, text)

text = puzzle_input_1.split("\n")
found = find_starting_letter(text)
