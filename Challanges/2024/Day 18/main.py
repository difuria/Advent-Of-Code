from Inputs.puzzle_inputs import puzzle_input_1
from Inputs.test_inputs import test_input_1

import sys

class RAMRun:
    def __init__(self, text: str, grid_size: tuple[int]) -> None:
        self.coordinates = self._get_coordinates(text)
        self.grid_size = grid_size

        self.start = (0,0)
        self.exit = (grid_size[0]-1, grid_size[1]-1)

        self.grid = self.define_grid()

    def _get_coordinates(self, text: str) -> list[tuple[int]]:
        coordinates = []
        for line in text.strip().splitlines():
            x, y = list(map(int, line.split(",")))
            coordinates.append((x, y))

        return coordinates

    def place_ram(self, fallen:int) -> None:
        for i in range(fallen):
            x, y = self.coordinates[i]
            self.grid[y][x] = "#"

    def define_grid(self) -> list[list[str]]:
        grid = []

        for y in range(self.grid_size[0]):
            current = []
            for x in range(self.grid_size[1]):
                current.append(".")
            grid.append(current)

        return grid
    
    def print_grid(self):
        for line in self.grid:
            cl = ""
            for char in line:
                cl += str(char)
            print(cl)
    
    def find_shorted_path(self):
        queue = []

        queue.append(self.start)

        movements = (
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        )

        shortest_path = sys.maxsize
        x, y = self.start
        self.grid[y][x] = 0
        while queue:
            cx, cy = queue.pop(0)


            for movement in movements:
                nx = cx + movement[0]
                ny = cy + movement[1]
                np = (nx, ny)

                ns = self.grid[cy][cx] + 1
                if ny < 0 or ny >= len(self.grid):
                    continue
                elif nx < 0 or nx >= len(self.grid[ny]):
                    continue
                elif self.grid[ny][nx] == "#":
                    continue
                elif self.grid[ny][nx] == ".":
                    self.grid[ny][nx] = ns
                elif self.grid[ny][nx] <= ns:
                    continue

                self.grid[ny][nx] = ns

                if np == self.exit:
                    shortest_path = min(shortest_path, ns)
                else:
                    queue.append(np)
        
        print(f"Shortest path found was {shortest_path}.")
                

    
trr = RAMRun(test_input_1, (7, 7))
trr.place_ram(12)
trr.find_shorted_path()

prr = RAMRun(puzzle_input_1, (71, 71))
prr.place_ram(1024)
prr.find_shorted_path()