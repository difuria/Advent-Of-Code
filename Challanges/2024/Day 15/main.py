from Inputs.puzzle_inputs import puzzle_input_1
from Inputs.test_inputs import test_inputs


class WarehouseWoes:
    def __init__(self, text_input: str, task: int = 1) -> None:
        self.task = task
        self.grid, self.movements = self._generate_grid(text_input)
        self.robot = self._find_robot()

    def _generate_grid(self, text_input: str) -> tuple[list[list[str]], list[str]]:
        g, m = text_input.strip().split("\n\n")

        grid = []
        for g_line in g.splitlines():
            if self.task == 1:
                grid.append(list(g_line))
            elif self.task == 2:
                current_line = []
                for char in g_line:
                    if char == "O":
                        current_line.append("[")
                        current_line.append("]")
                    elif char == "@":
                        current_line.append("@")
                        current_line.append(".")
                    else:
                        current_line.append(char)
                        current_line.append(char)
                grid.append(current_line)
            else:
                ValueError(f"Invalid task of {self.task}.")

        movements = []
        for m_line in m.splitlines():
            movements += list(m_line)
        
        return grid, movements
    
    def _find_robot(self) -> list[int]:
        for y, line in enumerate(self.grid):
            if "@" in line:
                return (line.index("@"), y)
    
    def analyse_movements(self):
        movs = {
            "<": (-1, 0),
            ">": (1, 0),
            "^": (0, -1),
            "v": (0, 1)
        }

        for movement in self.movements:
            old_x, old_y = self.robot
            mov = movs[movement] # translate the movement into directions 
            new_x = old_x + mov[0]
            new_y = old_y + mov[1]
            new_location = (new_x, new_y)

            if self.grid[new_y][new_x] == "O":
                self._move_o(new_location, mov)
            elif self.grid[new_y][new_x] in ["[", "]"]:
                if self.grid[new_y][new_x] == "[":
                    open_pos = new_location
                    close_pos = (new_x + 1, new_y)
                else:
                    open_pos = (new_x - 1, new_y)
                    close_pos = new_location

                if self._determine_if_movement_is_possible(open_pos, close_pos, mov):
                    self._move_brackets(open_pos, close_pos, mov)

            if self.grid[new_y][new_x] == "#":
                # Robot will hit a wall do nothing
                continue
            elif self.grid[new_y][new_x] == ".":
                self.grid[new_y][new_x] = "@"
                self.grid[old_y][old_x] = "."
                self.robot = new_location
            elif self.grid[new_y][new_x] in ["O", "[", "]"]:
                # We weren't able to move the ofending O so do nothing
                continue
            else:
                raise ValueError(f"Unknown object of {self.grid[new_y][new_x]} found at ({new_x}, {new_y}).")
            
    def _move_brackets(self, open_pos: list[int], close_pos: list[int], movement: tuple[int]) -> None:
        """
        We should only be moving a bracket if we know it's possible to move them all. 
        """
        new_open_x = open_pos[0] + movement[0]
        new_open_y = open_pos[1] + movement[1]
        new_open_pos = (new_open_x, new_open_y)

        new_close_x = close_pos[0] + movement[0]
        new_close_y = close_pos[1] + movement[1]
        new_close_pos = (new_close_x, new_close_y)

        new_close_char = self.grid[new_close_y][new_close_x]
        new_open_char = self.grid[new_open_y][new_open_x]

        if movement == (1, 0):
            # We're moving right so we only care about the closing position
            if new_close_char == "[":
                self._move_brackets(new_close_pos, (new_close_x + 1, new_close_y), movement)
        elif movement == (-1, 0):
            # We're moving left so we only care about the opening position
            if new_open_char == "]":
                self._move_brackets((new_open_x - 1, new_open_y), new_open_pos, movement)
        else:
            # Moving up or down we care about both
            if new_open_char == "[":
                cur_close_pos = (new_open_x + 1, new_open_y) 
                cur_open_pos = new_open_pos

                self._move_brackets(cur_open_pos, cur_close_pos, movement)

            if new_open_char == "]":
                cur_close_pos = new_open_pos
                cur_open_pos = (new_open_x - 1, new_open_y)

                self._move_brackets(cur_open_pos, cur_close_pos, movement)

            if new_close_char == "[":
                cur_close_pos = (new_close_x + 1, new_open_y)
                cur_open_pos = new_close_pos

                self._move_brackets(cur_open_pos, cur_close_pos, movement)

        old_open_x, old_open_y = open_pos
        old_close_x, old_close_y = close_pos

        self.grid[old_open_y][old_open_x] = "."
        self.grid[old_close_y][old_close_x] = "."

        self.grid[new_open_y][new_open_x] = "["
        self.grid[new_close_y][new_close_x] = "]"

    def _determine_if_movement_is_possible(self, open_pos: list[int], close_pos: list[int], movement: tuple[int]) -> bool:
        """
        Before we begin moving everything we need to determine if everything in the tree can be moved. As the 
        farthest left node won't move if the furtherest right is blocked. 
        """
        new_open_x = open_pos[0] + movement[0]
        new_open_y = open_pos[1] + movement[1]
        new_open_pos = (new_open_x, new_open_y)

        new_close_x = close_pos[0] + movement[0]
        new_close_y = close_pos[1] + movement[1]
        new_close_pos = (new_close_x, new_close_y)

        new_close_char = self.grid[new_close_y][new_close_x]
        new_open_char = self.grid[new_open_y][new_open_x]

        if new_open_char == "#" or new_close_char == "#":
            return False

        possible = True
        if movement == (1, 0):
            # We're moving right so we only care about the closing position
            if new_close_char == "[":
                possible = self._determine_if_movement_is_possible(new_close_pos, (new_close_x + 1, new_close_y), movement)
            elif new_close_char != ".":
                raise ValueError(f"Unknown character of {new_close_char} at {new_close_pos}.")
        elif movement == (-1, 0):
            # We're moving left so we only care about the opening position
            if new_open_char == "]":
                possible = self._determine_if_movement_is_possible((new_open_x - 1, new_open_y), new_open_pos, movement)
            elif new_open_char != ".":
                raise ValueError(f"Unknown character of {new_open_char} at {new_open_pos}.")
        else:
            # Moving up or down we care about both

            # If the above box lines up
            if new_open_char == "[":
                cur_close_pos = (new_open_x + 1, new_open_y) 
                cur_open_pos = new_open_pos

                possible = self._determine_if_movement_is_possible(cur_open_pos, cur_close_pos, movement)

            # The following 2 if's are for if the opposite brackets line up.
            if new_open_char == "]" and possible:
                cur_close_pos = new_open_pos
                cur_open_pos = (new_open_x - 1, new_open_y)

                possible = self._determine_if_movement_is_possible(cur_open_pos, cur_close_pos, movement)

            if new_close_char == "[" and possible:
                cur_close_pos = (new_close_x + 1, new_open_y)
                cur_open_pos = new_close_pos

                possible = self._determine_if_movement_is_possible(cur_open_pos, cur_close_pos, movement)   

        return possible
     
    def _move_o(self, o_location: tuple[int], movement: tuple[int]) -> None:
        """Recursively move O's that are blocked by other O's"""
        old_x, old_y = o_location
        new_x = old_x + movement[0]
        new_y = old_y + movement[1]

        if self.grid[new_y][new_x] == "O":
            self._move_o((new_x, new_y), movement)
        
        if self.grid[new_y][new_x] == ".":
            self.grid[new_y][new_x] = "O"
            self.grid[old_y][old_x] = "."
        elif self.grid[new_y][new_x] == "#":
            # Can't move so do nothing
            return
        elif self.grid[new_y][new_x] == "O":
            # We weren't able to move the ofending O so do nothing
            return
        else:
             raise ValueError(f"Unknown object of {self.grid[new_y][new_x]} found at ({new_x}, {new_y}).")
        
    def print_grid(self):
        for line in self.grid:
            print("".join(line))
        print()

    def sum_gps_coordinates(self) -> int:
        sum = 0
        for y, line in enumerate(self.grid):
            for x, char in enumerate(line):
                if char in ["O", "["]:
                    sum += (100 * y) + x
        
        print(f"Sum of GPS Coordinates is {sum}.")
        return sum


print("Task 1 ")
print("Test input small")
small_test_input = WarehouseWoes(test_inputs["small"]["Input"])
small_test_input.analyse_movements()
small_test_input.print_grid()
sum = small_test_input.sum_gps_coordinates()

print("\nTest input Large")
large_test_input = WarehouseWoes(test_inputs["large"]["Input"])
large_test_input.analyse_movements()
large_test_input.print_grid()
large_test_input.sum_gps_coordinates()

print("\nPuzzle input")
puzzle_input = WarehouseWoes(test_inputs["small"]["Input"])
puzzle_input.analyse_movements()
puzzle_input.print_grid()

print("Task 2 ")
print("Test input small")
large_test_input_2 = WarehouseWoes(test_inputs["large"]["Input"], 2)
large_test_input_2.analyse_movements()
large_test_input_2.print_grid()
sum = large_test_input_2.sum_gps_coordinates()

puzzle_input_2 = WarehouseWoes(puzzle_input_1, 2)
puzzle_input_2.analyse_movements()
puzzle_input_2.print_grid()
sum = puzzle_input_2.sum_gps_coordinates()