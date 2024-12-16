from Inputs.puzzle_inputs import puzzle_input_1
from Inputs.test_inputs import test_input_1

class ReindeerMaze:
    def __init__(self, text: str) -> None:
        self.grid = self._get_grid(text)
        self.start = self.find_start()

    def _get_grid(self, text: str) -> list[list[str]]:
        grid = []

        for line in text.strip().splitlines():
            grid.append(list(line.strip()))
        
        return grid
    
    def find_start(self) -> tuple[int]:
        for y, line in enumerate(self.grid):
            if "S" in line:
                # x, y, initial facing direction
                return (line.index("S"), y, 0)
    
    def find_paths(self) -> None:
        x, y, d = self.start
        seen = set()
        seen.add((x, y))
        # X, Y coordinates, facing direction
        paths = [[{
            "x": x,
            "y": y,
            "d": d, 
            "s": seen
        }]]

        movements = (
            (1, 0, "E"),
            (0, 1, "S"),
            (-1, 0, "W"),
            (0, -1, "N")
        )

        completed_paths = []
        while paths:
            current_path = paths.pop(0)
            c = current_path[-1]
            print(c)
            input()
            for i, movement in enumerate(movements):
                new_seen = c["s"].copy()
                new_x = c["x"] + movement[0]
                new_y = c["y"] + movement[1]
                new_pos = (new_x, new_y)

                if new_pos in new_seen:
                    # Don't return to a position we've already been in
                    print("Backtracking")
                    continue
                elif self.grid[new_y][new_x] == "#":
                    print("Blocked")
                    continue
                elif self.grid[new_y][new_x] == ".":
                    new_seen.add(new_pos)
                    current_path.append({
                        "x": new_x, 
                        "y": new_y,
                        "d": i,
                        "s": new_seen
                    })
                    paths.append(current_path)
                elif self.grid[new_y][new_x] == "E":
                    # Found the end of the maze
                    print("Found the end!!!!")
                    completed_paths.append(current_path)
                else:
                    raise ValueError(f"Invalid character of {self.grid[new_y][new_x]} found at {new_x, new_y}")
            
        print("Completed paths")
        for completed_path in completed_paths:
            print(completed_path)
        
        print(f"There are {len(completed_paths)} possible paths")
    

print("Test Input 1")
ti1 = ReindeerMaze(test_input_1)
print(ti1.grid)
ti1.find_paths()