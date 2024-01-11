import os, sys

class SliceIt:
    def __init__(self, claim):
        self.claim = claim.strip().split("\n")

    def draw_grid(self, output = False):
        x_highest, y_highest = 0, 0
        self.grid = []
        self.grid_clothes = []
        index_set = set()
        for claim in self.claim:
            info = claim.replace(":", "").replace("#", "").split()
            x_start, y_start = list(map(int, info[2].split(",")))
            x_grid, y_grid = list(map(int, info[3].split("x")))
            x_highest = max(x_highest, x_start + x_grid)
            y_highest = max(y_highest, y_start + y_grid)
            index_set.add(info[0])

        for y in range(y_highest + 1):
            self.grid.append(["." for x in range(x_highest + 1)])
            self.grid_clothes.append(["." for x in range(x_highest + 1)])

        overlapping = 0
        overlapping_dict = {}
        for claim in self.claim:
            info = claim.replace(":", "").replace("#", "").split()
            index = info[0]
            x_start, y_start = list(map(int, info[2].split(",")))
            x_grid, y_grid = list(map(int, info[3].split("x")))

            for y in range(y_start, y_start + y_grid):
                for x in range(x_start, x_start + x_grid):
                    if self.grid[y][x] != ".":
                        block_index = self.grid_clothes[y][x]
                        if block_index in index_set:
                            index_set.remove(block_index)
                        if index in index_set:
                            index_set.remove(index)
                        if self.grid[y][x] != "X":
                            overlapping += 1
                        self.grid[y][x] = "X"
                    else:
                        self.grid[y][x] = index
                        self.grid_clothes[y][x] = index
                        if not index in overlapping_dict:
                            overlapping_dict[index] = set()
        if output:
            for line in self.grid:
                print("".join(line))
            print()

        print(f"Overlapping claims: {overlapping}")
        print(f"Items with no overlapping claim: {index_set}")

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

    print("Test inputs:")
    slice_it = SliceIt(get_file(path, "test_claims_1.txt"))
    slice_it.draw_grid(True)

    print("\nPuzzle inputs:")
    slice_it = SliceIt(get_file(path, "puzzle_claims_1.txt"))
    slice_it.draw_grid()
