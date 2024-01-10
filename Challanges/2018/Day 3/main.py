import os, sys

input_text = "puzzle_claims_1.txt"

class SliceIt:
    def __init__(self, claim):
        self.claim = claim.strip().split("\n")

    def draw_grid(self):
        x_highest, y_highest = 0, 0
        self.grid = []
        for claim in self.claim:
            info = claim.replace(":", "").split()
            x_start, y_start = list(map(int, info[2].split(",")))
            x_grid, y_grid = list(list(map(int, info[3].split("x"))))
            x_highest = max(x_highest, x_start + x_grid)
            y_highest = max(y_highest, y_start + y_grid)

        for y in range(y_highest + 1):
            self.grid.append(["." for x in range(x_highest + 1)])

        overlapping = 0
        for claim in self.claim:
            info = claim.replace(":", "").split()
            index = info[0].replace("#", "")
            x_start, y_start = list(map(int, info[2].split(",")))
            x_grid, y_grid = list(list(map(int, info[3].split("x"))))

            for y in range(y_start, y_start + y_grid):
                for x in range(x_start, x_start + x_grid):
                    if self.grid[y][x] != ".":
                        if self.grid[y][x] != "X":
                            overlapping += 1
                        self.grid[y][x] = "X"
                    else:
                        self.grid[y][x] = index
                    
        for line in self.grid:
            print("".join(line))
        print()
        
        print(f"Overlapping claims: {overlapping}")

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

    slice_it = SliceIt(get_file(path, input_text))
    slice_it.draw_grid()
