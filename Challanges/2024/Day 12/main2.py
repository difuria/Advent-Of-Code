def get_number_of_sides(perimeter: list[tuple[int, int]]) -> int:
    """
    Calculate the number of unique sides for the region based on the perimeter.
    """
    sides = set()

    for x, y in perimeter:
        # Check the four directions and treat each as a unique "side"
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            segment = ((x, y), (x + dx, y + dy))
            # Add both orientations of the side to ensure they're treated uniquely
            sides.add(tuple(sorted(segment)))

    return len(sides)


def search_area_and_sides(start: tuple[int, int], grid: list[list[str]], seen: set[tuple[int, int]]) -> tuple[int, int]:
    """
    Find the area and number of sides for the region starting at `start`.
    """
    area = 0
    perimeter = []
    char = grid[start[1]][start[0]]  # Get the plant type for the region
    seen.add(start)
    queue = [start]

    movements = [
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1)
    ]

    while queue:
        x, y = queue.pop(0)
        area += 1

        for dx, dy in movements:
            new_x, new_y = x + dx, y + dy
            neighbor = (new_x, new_y)

            # Check if we are outside the grid
            if new_y < 0 or new_y >= len(grid) or new_x < 0 or new_x >= len(grid[new_y]):
                perimeter.append((x, y))
                continue

            # If the neighbor is a different type, add to perimeter
            if grid[new_y][new_x] != char:
                perimeter.append((x, y))
                continue

            # If the neighbor is unvisited and the same type, add to queue
            if neighbor not in seen:
                seen.add(neighbor)
                queue.append(neighbor)

    # Calculate the number of sides
    sides = get_number_of_sides(perimeter)
    return area, sides


def calculate_bulk_price(grid: list[list[str]]) -> int:
    """
    Calculate the total bulk price of fencing for all regions in the grid.
    """
    seen = set()
    total_price = 0

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            position = (x, y)
            if position in seen:
                continue

            # Calculate area and number of sides for the region
            area, sides = search_area_and_sides(position, grid, seen)
            total_price += area * sides

    return total_price


def solve_part_two(input_text: str) -> int:
    """
    Solve Part Two of the puzzle.
    """
    # Parse the input into a grid
    grid = [list(line) for line in input_text.strip().split("\n")]

    # Calculate the total bulk price
    return calculate_bulk_price(grid)
