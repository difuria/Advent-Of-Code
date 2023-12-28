import math, os, re, sys

input_text_task_1 = "puzzle_path_1.txt"
input_text_task_2 = "puzzle_path_1.txt"

class HauntedWasteland:
    def __init__(self):
        self.directions = ""
        self.path_directions = {}

    def extract_path_info(self, path):
        self.path_directions = {}
        self.directions, paths = path.split("\n\n")

        for path_info in paths.strip().split("\n"):
            key, LR = path_info.split("=")
            left, right = re.sub(r"(\(|\))", "", LR).split(",")
            self.path_directions[key.strip()] = { "L": left.strip(), "R": right.strip()}

    def run_path(self, start = "AAA", end = "ZZZ", output = True):
        # Solution to task 1 (Also used for task 2)
        steps = 0
        current_location = start
        direction_index = 0
        while True:
            direction = self.directions[direction_index]
            current_location = self.path_directions[current_location][direction]
            steps += 1

            if current_location[-len(end):] == end:
                if output:
                    print(f"Steps taken for {start} to {end} was {steps} steps.")
                return steps

            direction_index += 1
            if direction_index >= len(self.directions):
                direction_index = 0
    
    def run_ghost_path(self, start = "A", end = "Z"):
        # Solution to task 2
        ghost_current_location = []

        for path in self.path_directions:
            if path[-len(start)] == start:
                ghost_current_location.append(path)
        
        steps = []
        for ghost in ghost_current_location:
            steps.append(self.run_path(ghost, end, False))
        
        print(f"Ghost steps taken for {start} to {end} was {math.lcm(*steps)} steps.")

def get_file(task, path, file):
    file = os.path.join(path, f"Task {task} Inputs", file)

    if not os.path.exists(file):
        print(f"Invalid file supplied of {file}")
        sys.exit(1)

    with open(file, "r") as f:
        path_info = f.read()

    return path_info

if __name__ == "__main__":
    path = os.path.dirname(__file__)

    haunted_wasteland = HauntedWasteland()
    haunted_wasteland.extract_path_info(get_file(1, path, input_text_task_1))
    haunted_wasteland.run_path()

    haunted_wasteland.extract_path_info(get_file(2, path, input_text_task_2))
    haunted_wasteland.run_ghost_path()
