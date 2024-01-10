import math, os, sys

input_text = "puzzle_trees_1.txt"

class TobogganTrajectory:
    def __init__(self):
        self.map = []
    
    def load_map(self, map):
        self.map = [list(map_row) for map_row in map.strip().split("\n")]

    def trees_encountered(self, x_movement = 3, y_movement = 1):
        encountered_map = [row[:] for row in self.map]
        x, y = 0, 0
        trees_encountered = 0
        for i in range(math.ceil(len(self.map)/y_movement)):
            if encountered_map[y][x] == ".":
                encountered_map[y][x] = "O"
            elif encountered_map[y][x] == "#":
                encountered_map[y][x] = "X"
                trees_encountered += 1
            
            x += x_movement
            y += y_movement

            if y >= len(encountered_map):
                y = len(encountered_map) - 1

            if x >= len(encountered_map[y]):
                x = x - len(encountered_map[y])

        print(f"{trees_encountered} trees were encountered.")
        return trees_encountered

def get_file(path, file):
    file = os.path.join(path, f"Task Inputs", file)

    if not os.path.exists(file):
        print(f"Invalid file supplied of {file}")
        sys.exit(1)

    with open(file, "r") as f:
        path_info = f.read()

    return path_info

if __name__ == "__main__":
    path = os.path.dirname(__file__)

    toboggan_trajectory = TobogganTrajectory()
    toboggan_trajectory.load_map(get_file(path, input_text))
    toboggan_trajectory.trees_encountered()

    print()
    multiple_of_encounters = 1
    for movement in [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]:
        encountered = toboggan_trajectory.trees_encountered(movement[0], movement[1])
        if encountered > 0:
            multiple_of_encounters *= encountered
    
    print(f"Movement multiple is {multiple_of_encounters}")