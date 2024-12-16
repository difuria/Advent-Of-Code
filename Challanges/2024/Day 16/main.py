from Inputs.puzzle_inputs import puzzle_input_1
from Inputs.test_inputs import test_input_1, test_input_2

import sys

class ReindeerMaze:
    def __init__(self, text: str) -> None:
        self.grid = self._get_grid(text)
        self.start, self.end = self.find_start()

        self.completed_paths = []

    def _get_grid(self, text: str) -> list[list[str]]:
        grid = []

        for line in text.strip().splitlines():
            grid.append(list(line.strip()))
        
        return grid
    
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
                turn_score = abs(i - item["direction"])
                if turn_score == 3:
                    turn_score = 1
                
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

        print(f"Minimum score to the end is {min_score}.")


print("Task 1")
print("Test Inputs")
ti1 = ReindeerMaze(test_input_1)
ti1.find_paths()

ti2 = ReindeerMaze(test_input_2)
ti2.find_paths()

print("Puzzle Input")
p1 = ReindeerMaze(puzzle_input_1)
p1.find_paths()