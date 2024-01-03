import os, sys

input_text = "puzzle_pipes_1.txt"

class PipeMaze:
    def __init__(self):
        self.start = []
        self.maze = []
        self.maze_distances = []

        # y = Columns, x = Rows
        self.pipes = {
            "S": [[1, 0], [0, 1], [-1, 0], [0, -1]],
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
        # Now check for incompatible pipes
        distance = current_distance
        if not self.maze[y][x] in impassable:
            distance += 1
            self.maze_distances[y][x] = distance
            pipes.append([[y, x], current_position])
        return pipes, distance

    def print_maze_distances(self):
        # Making the length of everything the same makes debugging easier
        longest = 0
        out_put = []
        for line in self.maze_distances:
            for item in line:
                longest = max(longest, len(str(item)))
        
        for line in self.maze_distances:
            out_put.append([])
            for item in line:
                item = str(item)
                out_put[-1].append((' ' * (longest - len(item))) + item)

        for line in out_put:
            print(line)
        
        print("")

    def print_maze(self):
        for line in self.maze:
            print(line)
        
        print("")

    def follow_pipes(self):
        if not self.start:
            return

        pipes = [[self.start, self.start]]
        max_distance = 0
        self.maze_distances[self.start[0]][self.start[1]] = 0

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
    
    def __flood_fill_area(self, y, x, character = "X"):
        movements = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        locations = [[y, x]]
        count = 0
        if type(self.maze_distances[y][x]) != int:
            self.maze_distances[y][x] = character
            count += 1

        while locations:
            col, row = locations.pop(0)
            for y, x in movements:
                new_col = col + y
                new_row = row + x

                if 0 <= new_col and new_col < len(self.maze_distances) and 0 <= new_row and new_row < len(self.maze_distances[new_col])\
                      and (type(self.maze_distances[new_col][new_row]) != int and self.maze_distances[new_col][new_row] != character):
                    self.maze_distances[new_col][new_row] = character
                    locations.append([new_col, new_row])
                    count += 1
        
        return count

    def mark_inside_or_outside_loops(self):
        # For an enclosed shape, if you shoot a ray in any direction and it has to cross a boundary at odd amount of times it is within the shape
        # an even amount of times and it is within

        contained = 0
        not_contained = 0
        for y, row in enumerate(self.maze_distances):
            for x, col in enumerate(self.maze_distances[y]):
                if type(self.maze_distances[y][x]) != int and not self.maze_distances[y][x] in ["X", "O"]:      
                    # Shoot beam
                    right_down_diagonal  = 0
                    i = x +1
                    j = y + 1
                    while j < len(self.maze_distances) and i < len(self.maze_distances[j]):
                        if type(self.maze_distances[j][i]) == int and not self.maze[j][i] in ["L", "7"]:
                            right_down_diagonal += 1
                        i += 1
                        j += 1 

                    # Check both directions as you can also get off when shooting from the outside
                    if right_down_diagonal % 2 == 1 and y != 0 and x != 0 and y != len(self.maze_distances)-1 and x != len(self.maze_distances[y])-1:
                        contained += self.__flood_fill_area(y, x, "X")
                    else:
                        not_contained += self.__flood_fill_area(y, x, "O")

        print(f"Contained area is {contained}.")
        return contained

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

    for i in range(1, 9):
        pipe_maze.load_maze(get_file(path, f"test_pipes_{i}.txt"))
        pipe_maze.follow_pipes()
        contained = pipe_maze.mark_inside_or_outside_loops()

    pipe_maze.load_maze(get_file(path, input_text))
    pipe_maze.follow_pipes()
    pipe_maze.mark_inside_or_outside_loops()
