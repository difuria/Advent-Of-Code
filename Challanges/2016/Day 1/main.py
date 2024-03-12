import os, sys

def get_file(path, file):
    file = os.path.join(path, f"Task Inputs", file)

    if not os.path.exists(file):
        print(f"Invalid file supplied of {file}")
        sys.exit(1)

    with open(file, "r") as f:
        path_info = f.read()

    return path_info

def distance(path, _file):
    currently_facing = 0
    
    visited = set()
    revisited_first_location = False

    position = [0, 0]
    document = get_file(path, _file).strip().split(", ")
    for direction in document:
        turn, movement_amount = direction[0], int(direction[1:])
        
        if turn == "R":
            currently_facing += 1
            if currently_facing >= len(directions):
                currently_facing = 0
        if turn == "L":
            currently_facing -= 1
            if currently_facing < 0:
                currently_facing = len(directions) - 1
            
        compass = directions[currently_facing]

        # Looping only so the same code can be used in task 1 and 2
        for i in range(movement_amount):
            position[0] += movement[compass][0]
            position[1] += movement[compass][1]

            tuple_position = tuple(position)
            if tuple_position in visited and not revisited_first_location:
                blocks_away = abs(position[0]) + abs(position[1])
                print(f"You are {blocks_away} from the first revisited position.")
                revisited_first_location = True
            else:
                visited.add(tuple_position)

    return abs(position[0]) + abs(position[1])

if __name__ == "__main__":
    path = os.path.dirname(__file__)

    directions = ["N", "E", "S", "W"]
    movement = {
        "N": [0, 1],
        "E": [1, 0],
        "W": [-1, 0],
        "S": [0, -1]
    }

    test_answers = [5, 2, 12, 8]
    for i in range(1, 5):
        blocks_away = distance(path, f"test_document_{i}.txt")
        answer = "correct" if blocks_away == test_answers[i-1] else "incorrect."
        print(f"You are {blocks_away} which is {answer}.")

    blocks_away = distance(path, "puzzle_document_1.txt")
    print()
    print(f"For the puzzle you are {blocks_away}")