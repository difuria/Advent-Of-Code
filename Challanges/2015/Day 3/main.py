from Inputs.puzzle_inputs import puzzle_input_1
from Inputs.test_inputs import test_input_1, test_input_2, test_input_3, test_input_4


def determine_houses_visited(directions: str, robo_santa: bool = False):
    location = {
        "Santa": [0, 0],
        "Robo Santa": [0, 0]
    }

    visited = [location["Santa"][:]]

    for i, direction in enumerate(directions):
        key = "Santa"
        if robo_santa and i % 2 != 0:
            key = "Robo Santa"

        if direction == ">":
            location[key][0] += 1
        elif direction == "<":
            location[key][0] -= 1
        elif direction == "^":
            location[key][1] += 1
        elif direction == "v":
            location[key][1] -= 1

        if not location[key] in visited:
            visited.append(location[key][:])
    
    print(f"Visited {len(visited)} houses.")

print("Task 1")
determine_houses_visited(test_input_1)
determine_houses_visited(test_input_2)
determine_houses_visited(test_input_3)
determine_houses_visited(puzzle_input_1)

print("\nTask 2")
determine_houses_visited(test_input_4, True)
determine_houses_visited(test_input_2, True)
determine_houses_visited(test_input_3, True)
determine_houses_visited(puzzle_input_1, True)