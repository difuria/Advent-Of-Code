from Inputs.puzzle_inputs import puzzle_input_1
from Inputs.test_inputs import test_inputs


class WarehouseWoes:
    def __init__(self, text_input: str) -> None:
        self.grid, self.movements = self._generate_grid(text_input)
        self.robot = self._find_robot()

    def _generate_grid(self, text_input: str) -> tuple[list[list[str]], list[str]]:
        g, m = text_input.strip().split("\n\n")

        grid = []
        for g_line in g.splitlines():
            grid.append(list(g_line))

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

            if self.grid[new_y][new_x] == "#":
                # Robot will hit a wall do nothing
                continue
            elif self.grid[new_y][new_x] == ".":
                self.grid[new_y][new_x] = "@"
                self.grid[old_y][old_x] = "."
                self.robot = new_location
            elif self.grid[new_y][new_x] == "O":
                # We weren't able to move the ofending O so do nothing
                continue
            else:
                raise ValueError(f"Unknown object of {self.grid[new_y][new_x]} found at ({new_x, new_y}).")
            
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
             raise ValueError(f"Unknown object of {self.grid[new_y][new_x]} found at ({new_x, new_y}).")
        
    def print_grid(self):
        for line in self.grid:
            print("".join(line))
        print()

    def sum_gps_coordinates(self) -> int:
        sum = 0
        for y, line in enumerate(self.grid):
            for x, char in enumerate(line):
                if char == "O":
                    sum += (100 * y) + x
        
        print(f"Sum of GPS COordinates is {sum}.")
        return sum


small_test_input = WarehouseWoes(test_inputs["small"]["Input"])
small_test_input.analyse_movements()
small_test_input.print_grid()
sum = small_test_input.sum_gps_coordinates()

large_test_input = WarehouseWoes(test_inputs["large"]["Input"])
large_test_input.analyse_movements()
large_test_input.print_grid()
large_test_input.sum_gps_coordinates()

puzzle_input = WarehouseWoes(puzzle_input_1)
puzzle_input.analyse_movements()
puzzle_input.print_grid()
puzzle_input.sum_gps_coordinates()