import os, re, sys

input_text_task_1 = "puzzle_path_1.txt"

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

    def run_path(self, start = "AAA", end = "ZZZ"):
        # Solution to task 1
        steps = 0
        current_location = start
        direction_index = 0
        while True:
            direction = self.directions[direction_index]
            current_location = self.path_directions[current_location][direction]
            steps += 1

            if current_location == end:
                print(f"Steps taken {steps}.")
                return

            direction_index += 1
            if direction_index >= len(self.directions):
                direction_index = 0

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
