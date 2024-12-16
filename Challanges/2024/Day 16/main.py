from Inputs.puzzle_inputs import puzzle_input_1
from Inputs.test_inputs import test_input_1, test_input_2

import sys

class ReindeerMaze:
    def __init__(self, text: str) -> None:
        self.grid, self.og = self._get_grid(text)
        self.start, self.end = self.find_start()

        self.completed_paths = []

    def _get_grid(self, text: str) -> list[list[str]]:
        grid = []
        og = []

        for line in text.strip().splitlines():
            grid.append(list(line.strip()))
            og.append(list(line.strip()))
        
        return grid, og
    
    def find_start(self) -> tuple[int]:
        start = None
        end = None
        for y, line in enumerate(self.grid):
            if "S" in line:
                start = (line.index("S"), y)
            if "E" in line:
                end = (line.index("E"), y)
            
            if start and end:
                return start, end
    
    def find_paths(self) -> None:
        movements = (
            (1, 0, "E"),
            (0, 1, "S"),
            (-1, 0, "W"),
            (0, -1, "N")
        )

        print("Starting at:", self.start, "Ending at:", self.end)
        queue = []
        position = {
            "position": self.start,
            "direction": 0,
            "score": 0
        }
        queue.append(position)

        x, y = self.start
        self.grid[y][x] = position

        min_score = sys.maxsize
        while queue:
            # Find the path using Dijkstra's algorithm. Keep track of the paths on the grid itself
            item = queue.pop(0)
            
            for i, movement in enumerate(movements):
                new_x = item["position"][0] + movement[0]
                new_y = item["position"][1] + movement[1]
                new_pos = (new_x, new_y)
                turn_score = abs(i - item["direction"]) % 2  # Will only be a single turn or no turn
                new_score = item["score"] + 1 + (1000 * turn_score)

                position = {
                    "position": (new_pos),
                    "direction": i,
                    "score": new_score
                }

                if self.grid[new_y][new_x] in ["#"]:
                    # Deadend 
                    continue
                elif self.grid[new_y][new_x] in [".", "E"]:
                    self.grid[new_y][new_x] = position
                    queue.append(position)  
                elif self.grid[new_y][new_x]["score"] < new_score:
                    # Current grid score is lower than what we've got so we can ignore
                    continue
                else:
                    self.grid[new_y][new_x] = position
                    queue.append(position)
                
                if new_pos == self.end:
                    min_score = min(min_score, position["score"])

        print("Score", self.grid[7][3])
        print(f"Minimum score to the end is {min_score}.")

    def find_tiles_in_shorest_path(self):
        queue = [{
            "position": self.end, 
            "path": {self.end}
        }]

        movements = (
            (1, 0),
            (0, 1),
            (-1, 0),
            (0, -1)
        )

        shorted_path_tiles = set()
        # We need to ensure we reach the starting position again
        while queue:
            item = queue.pop(0)
            x, y = item["position"]
            cur_score = self.grid[y][x]["score"]

            for movement in movements:
                new_x = x + movement[0]
                new_y = y + movement[1]
                new_pos = (new_x, new_y)

                if self.grid[new_y][new_x] == "#":
                    continue
                elif new_y < 0 or new_y > len(self.grid):
                    continue
                elif new_x < 0 or new_x > len(self.grid[new_y]):
                    continue

                new_score = self.grid[new_y][new_x]["score"]

                potential_scores = [
                    cur_score - 1,
                    cur_score - 1 - 1000
                ]

                # From the end posiion we should only be going down
                if (x, y) != self.end:
                    potential_scores.append(cur_score - 1 + 1000) # Fewer turns could be used at a later time)

                if new_score in potential_scores:
                    new_path = item["path"].copy()
                    new_path.add(new_pos)
                    new_item = {
                        "path": new_path,
                        "position": (new_x, new_y)
                    }
                    
                    if new_score == 0:
                        # We're at the end
                        shorted_path_tiles.update(new_item["path"])
                    else:
                        queue.append(new_item)

        print(f"\nThere are {len(shorted_path_tiles)} tiles that can be in the shortest path.")

        for y, line in enumerate(self.grid):
            p_line = ""
            for x, char in enumerate(line):
                if (x,y) in shorted_path_tiles:
                    p_line += "O"
                else:
                    p_line += self.og[y][x]
            print(p_line)

print("Test Inputs")
ti1 = ReindeerMaze(test_input_1)
ti1.find_paths()
ti1.find_tiles_in_shorest_path()

ti2 = ReindeerMaze(test_input_2)
ti2.find_paths()
ti2.find_tiles_in_shorest_path()

print("Puzzle Input")
p1 = ReindeerMaze(test_input_1)
p1.find_paths()
p1.find_tiles_in_shorest_path()

# 703 is too high