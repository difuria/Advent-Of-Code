import os, sys

input_text = "puzzle_pipes_1.txt"

class PipeMaze:
    def __init__(self):
        self.start = []
        self.maze = []
        self.maze_distances = []

        # y = Columns, x = Rows
        self.pipes = {
            "-": [[0, 1], [0, -1]],
            "|": [[1, 0], [-1, 0]],
            "F": [[1, 0], [0, 1]],
            "L": [[0, 1], [-1, 0]],
            "7": [[1, 0], [0, -1]],
            "J": [[-1, 0], [0, -1]],
        }

        self.invalid_movements = {
            "x": {
                1: { "|", "F", "L" },
                -1: { "|", "7", "J" }
            },
            "y": {
                1: { "-", "F", "7" },
                -1: { "L", "-", "J" }
            },
        }
    
    def load_maze(self, maze):
        self.maze = [list(row.strip()) for row in maze.strip().split("\n")]
        self.start = []
        self.maze_distances = []
        for col_index, row in enumerate(self.maze):
            if "S" in row:
                row_index = row.index("S")
                self.start = [col_index, row_index]
                break
        
        self.maze_distances = [m[:] for m in self.maze]

    def __check_potentially_valid_pipe(self, previous_position, y, x):
        return ( \
                   ( y >= 0 and y < len(self.maze) ) and \
                   ( x >= 0 and x < len(self.maze[y]) ) and \
                   self.maze[y][x] != "." and \
                   previous_position != [y, x] and \
                   self.maze_distances[y][x] != 0 and \
                   (\
                       (\
                           type(self.maze_distances[y][x]) == int and self.maze_distances[y][x] != self.maze_distances[previous_position[0]][previous_position[1]] \
                       )\
                       or \
                       type(self.maze_distances[y][x]) == str \
                   )\
                )

    def __check_valid_for_given_pipe(self, current_position, y, x, current_distance, impassable, pipes):
        # Now check for incompatiable pipes
        distance = current_distance
        if not self.maze[y][x] in impassable:
            distance += 1
            self.maze_distances[y][x] = distance
            pipes.append([[y, x], current_position])
        return pipes, distance

    def print_maze_distances(self):
        for line in self.maze_distances:
            print(line)
        
        print("")

    def print_maze(self):
        for line in self.maze:
            print(line)
        
        print("")

    def follow_pipes(self):
        if not self.start:
            return

        pipes = []
        max_distance = 0
        self.maze_distances[self.start[0]][self.start[1]] = 0
        for i, j in [[0,1], [1,0], [-1,0], [0, -1]]:
            x = i + self.start[1]
            y = j + self.start[0]

            if y < 0 or y >= len(self.maze) or x < 0 or x >= len(self.maze[y]):
                continue

            # Check we're not moving into an invalid pipe
            if (i == 1 and self.maze[y][x] in self.invalid_movements["x"][1]) or \
               (i == -1 and self.maze[y][x] in self.invalid_movements["x"][-1]) or \
               (j == 1 and self.maze[y][x] in self.invalid_movements["y"][1]) or \
               (j == -1 and self.maze[y][x] in self.invalid_movements["y"][-1]):
                continue

            if self.maze[y][x] != ".":
                pipes.append([[y, x], self.start])
                self.maze_distances[y][x] = 1
                max_distance = 1

        while pipes:
            current_position, previous_position = pipes.pop(0)
            current_y, current_x = current_position

            current_distance = self.maze_distances[current_y][current_x]
            current_pipe = self.maze[current_y][current_x]

            if current_pipe in self.pipes:
                for movement in self.pipes[current_pipe]:
                    y_movement, x_movement = movement
                    potential_x = current_x + x_movement
                    potential_y = current_y + y_movement

                    impassable = []
                    if x_movement in self.invalid_movements["x"]:
                        impassable = self.invalid_movements["x"][x_movement]
                    elif y_movement in self.invalid_movements["y"]:
                        impassable = self.invalid_movements["y"][y_movement]

                    if self.__check_potentially_valid_pipe(previous_position, potential_y, potential_x):
                        pipes, distance = self.__check_valid_for_given_pipe(current_position, potential_y, potential_x, current_distance, impassable, pipes)
                        max_distance = max(max_distance, distance)
        
        print(f"Max distance found was {max_distance}")
        return max_distance

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

    pipe_maze = PipeMaze()

    for i in range(1, 8):
        pipe_maze.load_maze(get_file(path, f"test_pipes_{i}.txt"))
        pipe_maze.follow_pipes()
    
    pipe_maze.load_maze(get_file(path, input_text))
    pipe_maze.follow_pipes()