from Inputs.test import t1
from Inputs.puzzle import p1


def create_grid(diagram: str) -> list[list[str]]:
    grid: list[list[str]] = []
    for row in diagram.strip().splitlines():
        grid.append(list(row))
    
    return grid[:]


def find_start(grid: list[list[str]]) -> tuple[int]:
    for y, row in enumerate(grid):
        for x, col in enumerate(row):
            if col == "S":
                return x, y
    
    return -1, -1


def quantum_beam_paths(diagram:str) -> int:
    grid: list[list[str]] = create_grid(diagram)

    current_beams: list[tuple[int]] = [find_start(grid)]  # Create a stack of beams
    splits: int = 0

    while current_beams:
        cur_x, cur_y = current_beams.pop(0)
        new_y: int = cur_y + 1

        if new_y >= len(grid):
            continue  # We've reach the bottom
        elif grid[new_y][cur_x] == "|": 
            continue  # We've seen this before so we can skip
        elif grid[new_y][cur_x] == ".":
            current_beams.append((cur_x, new_y))
            grid[new_y][cur_x] = "|"
        elif grid[new_y][cur_x] == "^":
            splits += 1
            for new_x in [cur_x - 1, cur_x + 1]:
                if grid[new_y][new_x] == ".":
                    current_beams.append((new_x, new_y))
                    grid[new_y][new_x] = "|"
        else:
            raise ValueError(f"Unhandled value at ({cur_x}, {new_y})")

    for row in grid:
        print("".join(row))
    
    return splits


def number_of_beam_paths(diagram:str) -> int:
    grid: list[list[str]] = create_grid(diagram)
    x, y = find_start(grid)

    seen: dict[int, dict[int, int]] = {}
    def find_paths(x: int, y: int):
        if seen.get(y, {}).get(x, None):
            return seen.get(y, {}).get(x, None)
        
        new_y: int = y + 1
        if new_y >= len(grid):
            return 1

        found: int = 0
        if grid[new_y][x] == ".":
            found += find_paths(x, new_y)
        elif grid[new_y][x] == "^":
            found += find_paths(x - 1, new_y)
            found += find_paths(x + 1, new_y)

        if y not in seen:
            seen[y] = {}

        if x not in seen[y]:
            seen[y][x] = found

        return seen[y][x]
    
    return find_paths(x, y)


print("Task 1:")
print(f"There were {quantum_beam_paths(t1)} splits in the test.")
print(f"There were {quantum_beam_paths(p1)} splits in the puzzle.")

print("\nTask 2:")
print(f"There were {number_of_beam_paths(t1)} possible paths in the test.")
print(f"There were {number_of_beam_paths(p1)} possible paths in the puzzle.")