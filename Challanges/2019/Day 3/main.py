import os, sys

input_text = "test_wires_1.txt"

class CrossedWires:
    def __init__(self, wires):
        self.wires = wires.strip().split("\n")

        self.map = []
        self.positions = {
            "min": { "x": 0, "y": 0 },
            "max": { "x": 0, "y": 0 }
        }

    def find_starting_position(self):
        self.positions = {
            "min": { "x": 0, "y": 0 },
            "max": { "x": 0, "y": 0 }
        }
        # [x, y]
        current_position = [0, 0]
        for wire in self.wires:
            for direction in wire.split(","):
                if direction[0] == "U":
                    current_position[1] -= int(direction[1:])
                elif direction[0] == "D":
                    current_position[1] += int(direction[1:])
                elif direction[0] == "L":
                    current_position[0] -= int(direction[1:])
                elif direction[0] == "R":
                    current_position[0] += int(direction[1:])

                
                self.positions["min"]["x"] = min(current_position[0], self.positions["min"]["x"])
                self.positions["min"]["y"] = min(current_position[1], self.positions["min"]["y"])
                self.positions["max"]["x"] = max(current_position[0], self.positions["max"]["x"])
                self.positions["max"]["y"] = max(current_position[1], self.positions["max"]["y"])

    
    def draw_map(self, print_map = False):
        self.map = []
        self.both_wires_map = []
        # + 2 is just for spacing to make it visible
        for y in range(0, self.positions["max"]["y"] - self.positions["min"]["y"] + 2):
            self.map.append([" "] * (self.positions["max"]["x"] - self.positions["min"]["x"] + 2))
            self.both_wires_map.append([" "] * (self.positions["max"]["x"] - self.positions["min"]["x"] + 2))

        starting_position = [0, 0]
        if self.positions["min"]["x"] == 0:
            starting_position[0] = 1
        elif self.positions["max"]["x"] == 0:
            starting_position[0] = len(self.map) - 2
        else:
            starting_position[0] += abs(self.positions["min"]["x"]) + 1

        if self.positions["min"]["y"] >= 0:
            starting_position[1] = 1
        elif self.positions["max"]["y"] == 0:
            starting_position[1] = len(self.map) - 2
        else:
            starting_position[1] += abs(self.positions["min"]["y"]) + 1

        x, y = starting_position
        self.map[y][x] = "O"
        self.both_wires_map[y][x] = "O"

        crossing_points = []
        for i, wire in enumerate(self.wires):
            current_position = starting_position[:]
            for direction in wire.split(","):
                movement = int(direction[1:])
                for j in range(0, movement):
                    character = "-"
                    if direction[0] == "U":
                        current_position[1] -= 1
                        character = "|"
                    elif direction[0] == "D":
                        current_position[1] += 1
                        character = "|"
                    elif direction[0] == "L":
                        current_position[0] -= 1
                    elif direction[0] == "R":
                        current_position[0] += 1

                    x, y = current_position

                    if i == 0:
                        self.map[y][x] = character
                        if j == movement - 1:
                            self.map[y][x] = "+"
                    
                    self.both_wires_map[y][x] = character
                    if j == movement - 1:
                        self.both_wires_map[y][x] = "+"

                    if i == 1:
                        if self.map[y][x] != " ":
                            self.both_wires_map[y][x] = "X"
                            crossing_points.append([x, y])

        if print_map:
            self.print_map(self.map)
            self.print_map(self.both_wires_map)

        smallest_manhattan_distance = float('inf')
        for x, y in crossing_points:
            manhattan_distance = abs(x - starting_position[0]) + abs(y - starting_position[1])
            smallest_manhattan_distance = min(smallest_manhattan_distance, manhattan_distance)
        
        print(f"Manhattan Distance Was {smallest_manhattan_distance}")

    def print_map(self, map):
        for line in map:
            print("".join(line))
        print()

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

    crossed_wires = CrossedWires(get_file(path, "test_wires_1.txt"))
    crossed_wires.find_starting_position()
    crossed_wires.draw_map(True)

    crossed_wires = CrossedWires(get_file(path, "puzzle_wires_1.txt"))
    crossed_wires.find_starting_position()
    crossed_wires.draw_map()