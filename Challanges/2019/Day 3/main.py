import os, sys

input_text = "test_wires_1.txt"

class CrossedWires:
    def __init__(self, wires):
        self.wires = wires.strip().split("\n")

        self.first_wire_map = []
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

    def __move(self, direction, current_position):
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

        return current_position, character

    def draw_map(self, print_map = False):
        self.first_wire_map = []
        self.both_wires_map = []
        # + 2 is just for spacing to make it visible
        for y in range(0, self.positions["max"]["y"] - self.positions["min"]["y"] + 2):
            self.first_wire_map.append([" "] * (self.positions["max"]["x"] - self.positions["min"]["x"] + 2))
            self.both_wires_map.append([" "] * (self.positions["max"]["x"] - self.positions["min"]["x"] + 2))

        self.starting_position = [0, 0]
        if self.positions["min"]["x"] == 0:
            self.starting_position[0] = 1
        elif self.positions["max"]["x"] == 0:
            self.starting_position[0] = len(self.first_wire_map) - 2
        else:
            self.starting_position[0] += abs(self.positions["min"]["x"]) + 1

        if self.positions["min"]["y"] >= 0:
            self.starting_position[1] = 1
        elif self.positions["max"]["y"] == 0:
            self.starting_position[1] = len(self.first_wire_map) - 2
        else:
            self.starting_position[1] += abs(self.positions["min"]["y"]) + 1

        x, y = self.starting_position
        self.first_wire_map[y][x] = "O"
        self.both_wires_map[y][x] = "O"

        crossing_points = []
        for i, wire in enumerate(self.wires):
            current_position = self.starting_position[:]
            split_wires = wire.split(",")
            for j, direction in enumerate(split_wires):
                movement = int(direction[1:])
                for k in range(0, movement):
                    current_position, character = self.__move(direction, current_position)

                    x, y = current_position

                    self.both_wires_map[y][x] = character
                    if k == movement - 1 and j < len(split_wires) - 1:
                        self.both_wires_map[y][x] = "+"

                    if i == 0:
                        self.first_wire_map[y][x] = character
                        if k == movement - 1 and j < len(split_wires) - 1:
                            self.first_wire_map[y][x] = "+"
                    elif i == 1:
                        if self.first_wire_map[y][x] != " ":
                            self.both_wires_map[y][x] = "X"
                            crossing_points.append([x, y])

        if print_map:
            self.print_map(self.first_wire_map)
            self.print_map(self.both_wires_map)

        smallest_manhattan_distance = float('inf')
        for x, y in crossing_points:
            manhattan_distance = abs(x - self.starting_position[0]) + abs(y - self.starting_position[1])
            smallest_manhattan_distance = min(smallest_manhattan_distance, manhattan_distance)
        
        print(f"Manhattan Distance Was {smallest_manhattan_distance}")

    def print_map(self, map):
        for line in map:
            print("".join(line))
        print()

    def walk_map(self):
        distance_to_crossing_positions = {}
        for i, wire in enumerate(self.wires):
            current_position = self.starting_position[:]
            split_wires = wire.split(",")
            distance = 0
            for j, direction in enumerate(split_wires):
                movement = int(direction[1:])
                for k in range(0, movement):
                    current_position, character = self.__move(direction, current_position)
                    x, y = current_position
                    distance += 1
                    if self.both_wires_map[y][x] == "X":
                        if x not in distance_to_crossing_positions:
                            distance_to_crossing_positions[x] = { }
                        if y not in distance_to_crossing_positions[x]:
                            distance_to_crossing_positions[x][y] = { }
                        distance_to_crossing_positions[x][y][i] = distance

        shortest_distance = float('inf')
        for x, x_value in distance_to_crossing_positions.items():
            for y, y_value in x_value.items():
                total_distance = 0
                for wire, steps in y_value.items():
                    total_distance += steps
                
                shortest_distance = min(shortest_distance, total_distance)
     
        print(f"Shortest distance to an intersection is {shortest_distance}")

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
    crossed_wires.walk_map()

    crossed_wires = CrossedWires(get_file(path, "puzzle_wires_1.txt"))
    crossed_wires.find_starting_position()
    crossed_wires.draw_map()
    crossed_wires.walk_map()