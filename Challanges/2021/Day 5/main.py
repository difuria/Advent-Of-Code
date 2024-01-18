import os, sys

class HydrothermalVents:
    def __init__(self, line_segments):
        self.line_segments = []
        self.largest = { "x": 0, "y": 0 }
        for line in line_segments.strip().split("\n"):
            start, end = line.split(" -> ")
            start = list(map(int, start.split(",")))
            end = list(map(int, end.split(",")))

            self.largest["x"] = max(self.largest["x"], start[0], end[0])
            self.largest["y"] = max(self.largest["y"], start[1], end[1])
            self.line_segments.append([start, end])
        
        self.grid = []
        for y in range(self.largest["y"] + 1):
            self.grid.append(["."][:] * (self.largest["x"] + 1))

    def draw_straight_lines(self, print_output = True):
        overlapping_points = 0
        for segment in self.line_segments:
            start, end = segment
            if not (start[0] == end[0] or start[1] == end[1]):
                # This isn't a straight line
                continue

            if start[1] != end[1]:
                x = start[0]
                movement = -1 if start[1] > end[1] else 1
                for y in range(start[1], end[1] + movement, movement):
                    if self.grid[y][x] == ".":
                        self.grid[y][x] = 0
                    elif self.grid[y][x] == 1:
                        overlapping_points += 1
                    self.grid[y][x] += 1
            elif start[0] != end[0]:
                y = start[1]
                movement = -1 if start[0] > end[0] else 1
                for x in range(start[0], end[0] + movement, movement):
                    if self.grid[y][x] == ".":
                        self.grid[y][x] = 0
                    elif self.grid[y][x] == 1:
                        overlapping_points += 1
                    self.grid[y][x] += 1
        
        if print_output:
            for line in self.grid:
                output = ""
                for item in line:
                    output += str(item)
                print(output)
        
        print(f"There were {overlapping_points} overlapping points.")

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

    print("Test Inputs")
    hydrothermal_vents = HydrothermalVents(get_file(path, "test_vents_1.txt"))
    hydrothermal_vents.draw_straight_lines()

    print("\nPuzzle Inputs")
    hydrothermal_vents = HydrothermalVents(get_file(path, "puzzle_vents_1.txt"))
    hydrothermal_vents.draw_straight_lines(False)
