import os, sys

input_text = "test_pipes_1 copy.txt"
input_text = "puzzle_pipes_1.txt"

class PipeMaze:
    def __init__(self):
        self.start = []
        self.maze = []
        self.maze_distances = []

        # Positions you can move if you're on the pipe
        # x = Rows, y = Columns
    
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
        if not self.maze[y][x] in impassable:
            self.maze_distances[y][x] = current_distance + 1
            if current_distance + 1 == 6852:
                print(f"Current position {current_position} was {self.maze[current_position[0]][current_position[1]]}")
                print(f"Now at {self.maze[y][x]} Co: {y} {x}")
            pipes.append([[y, x], current_position])
        return pipes

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

        invalid_x_increase_positions = ["|", "F", "L"]
        invalid_x_decrease_positions = ["|", "7", "J"]
        invalid_y_increase_positions = ["-", "F", "7"]
        invalid_y_decrease_positions = ["L", "-", "J"]

        pipes = []
        self.maze_distances[self.start[0]][self.start[1]] = 0
        for i, j in [[0,1], [1,0], [-1,0], [0, -1]]:
            x = i + self.start[1]
            y = j + self.start[0]

            if (y < 0 or y >= len(self.maze)) or \
                (x < 0 or x >= len(self.maze[y])):
                continue

            # Check we're not moving into an invalid pipe
            if (i == 1 and self.maze[y][x] in invalid_x_increase_positions) or \
               (i == -1 and self.maze[y][x] in invalid_x_decrease_positions) or \
               (j == 1 and self.maze[y][x] in invalid_y_increase_positions) or \
               (j == -1 and self.maze[y][x] in invalid_y_decrease_positions):
                continue

            if self.maze[y][x] != ".":
                pipes.append([[y, x], self.start])
                self.maze_distances[y][x] = 1

        while pipes:
            current_position, previous_position = pipes.pop(0)
            current_y, current_x = current_position

            current_distance = self.maze_distances[current_y][current_x]
            current_pipe = self.maze[current_y][current_x]

            if current_pipe == "-":
                potential_x = current_x + 1            
                if self.__check_potentially_valid_pipe(previous_position, current_y, potential_x):
                    pipes = self.__check_valid_for_given_pipe(current_position, current_y, potential_x, current_distance, invalid_x_increase_positions, pipes)

                potential_x = current_x - 1
                if self.__check_potentially_valid_pipe(previous_position, current_y, potential_x):
                    pipes = self.__check_valid_for_given_pipe(current_position, current_y, potential_x, current_distance, invalid_x_decrease_positions, pipes)

            elif current_pipe == "|":
                potential_y = current_y + 1
                if self.__check_potentially_valid_pipe(previous_position, potential_y, current_x):
                    pipes = self.__check_valid_for_given_pipe(current_position, potential_y, current_x, current_distance, invalid_y_increase_positions, pipes)

                potential_y = current_y - 1
                if self.__check_potentially_valid_pipe(previous_position, potential_y, current_x):
                    pipes = self.__check_valid_for_given_pipe(current_position, potential_y, current_x, current_distance, invalid_y_decrease_positions, pipes)

            elif current_pipe == "F":
                potential_x = current_x + 1
                if self.__check_potentially_valid_pipe(previous_position, current_y, potential_x):
                    pipes = self.__check_valid_for_given_pipe(current_position, current_y, potential_x, current_distance, invalid_x_increase_positions, pipes)

                potential_y = current_y + 1
                if self.__check_potentially_valid_pipe(previous_position, potential_y, current_x):
                    pipes = self.__check_valid_for_given_pipe(current_position, potential_y, current_x, current_distance, invalid_y_increase_positions, pipes)

            elif current_pipe == "L":
                potential_x = current_x + 1
                if self.__check_potentially_valid_pipe(previous_position, current_y, potential_x):
                    pipes = self.__check_valid_for_given_pipe(current_position, current_y, potential_x, current_distance, invalid_x_increase_positions, pipes)

                potential_y = current_y - 1
                if self.__check_potentially_valid_pipe(previous_position, potential_y, current_x):
                    pipes = self.__check_valid_for_given_pipe(current_position, potential_y, current_x, current_distance, invalid_y_decrease_positions, pipes)

            elif current_pipe == "7":
                potential_x = current_x - 1
                if self.__check_potentially_valid_pipe(previous_position, current_y, potential_x):
                    pipes = self.__check_valid_for_given_pipe(current_position, current_y, potential_x, current_distance, invalid_x_decrease_positions, pipes)

                potential_y = current_y + 1
                if self.__check_potentially_valid_pipe(previous_position, potential_y, current_x):
                    pipes = self.__check_valid_for_given_pipe(current_position, potential_y, current_x, current_distance, invalid_y_increase_positions, pipes)

            elif current_pipe == "J":
                potential_x = current_x - 1
                if self.__check_potentially_valid_pipe(previous_position, current_y, potential_x):
                    pipes = self.__check_valid_for_given_pipe(current_position, current_y, potential_x, current_distance, invalid_x_decrease_positions, pipes)

                potential_y = current_y - 1
                if self.__check_potentially_valid_pipe(previous_position, potential_y, current_x):
                    pipes = self.__check_valid_for_given_pipe(current_position, potential_y, current_x, current_distance, invalid_y_decrease_positions, pipes)

        # self.print_maze()
        # self.print_maze_distances()

        max_distance = 0
        for line in self.maze_distances:
            for column in line:
                if type(column) == int:
                    max_distance = max(max_distance, column)
        
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

    for i in range(1, 5):
        pipe_maze.load_maze(get_file(path, f"test_pipes_{i}.txt"))
        pipe_maze.follow_pipes()
    
    pipe_maze.load_maze(get_file(path, input_text))
    pipe_maze.follow_pipes()