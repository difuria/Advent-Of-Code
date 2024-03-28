import os, sys

def get_file(path:str, file:str) -> str:
    file = os.path.join(path, f"Task Inputs", file)

    if not os.path.exists(file):
        print(f"Invalid file supplied of {file}")
        sys.exit(1)

    with open(file, "r") as f:
        path_info = f.read()

    return path_info

def get_floor(path:str, file:str) -> None:
    directions = get_file(path, file)
    floor = directions.count("(") - directions.count(")")
    print(f"{directions} results in floor {floor}")

def find_floor_position(path:str, file:str, desired_floor:int=-1) -> None:
    directions = get_file(path, file)
    
    floor = 0
    for i, direction in enumerate(directions):
        if direction == "(":
            floor += 1
        else:
            floor -= 1

        if floor == desired_floor:
            print(f"Position for {desired_floor} is {i+1}.")
            break

if __name__ == "__main__":
    path = os.path.dirname(__file__)

    print("Task 1")
    for i in range(1, 10):
        get_floor(path, f"task_1_input_{i}.txt")        

    print("Puzzle")
    get_floor(path, f"puzzle_input_1.txt")

    print("\nTask 2")
    for i in range(1, 3):
        find_floor_position(path, f"task_2_input_{i}.txt")

    print("Puzzle")
    find_floor_position(path, f"puzzle_input_1.txt")