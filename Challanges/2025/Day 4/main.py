from Inputs.test import t1
from Inputs.puzzle import p1


def find_paper(movement: tuple[int], row:int, col:int, locations: list[str]) -> int:
    row += movement[0]
    col += movement[1]
    
    if row < 0 or row >= len(locations): 
        return 0
    elif col < 0 or col >= len(locations[row]):
        return 0
    elif locations[row][col] == ".":
        return 0
    else:
        return 1


def locate_paper(locations: str, max_adjacet_rolls: int = 3, output: bool = False) -> tuple[int, list[list[str]]]:
    map: list[list[str]] = []
    for row in locations.strip().splitlines():
        map.append([])
        for col in row:
                map[-1].append("." if col == "x" else col)

    movements: tuple[tuple[int]] = (
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1),
        (1, 1),
        (1, -1),
        (-1, 1),
        (-1, -1),
    )

    count: int = 0
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] != "@":
                continue

            adjacent_paper_count: int = 0
            for movement in movements:
                adjacent_paper_count += find_paper(movement, y, x, map)
                if adjacent_paper_count > max_adjacet_rolls:
                    break  # No point looking anymore

            if adjacent_paper_count <= max_adjacet_rolls:
                map[y][x] = "x"
                count += 1

    out: str = ""
    for row in map:
        out += "".join(row).strip() + "\n"
    out = out.strip()

    if output:
        print(out + "\n")

    return count, out


def determine_total_to_remove(map: str, output: bool = False) -> int:
    old_map: int = ""
    total: int = 0
    current_map: str = map.strip()
    while old_map != current_map:
        old_map = current_map

        moved, current_map = locate_paper(current_map, output=output)
        total += moved
    
    return total


print("Task 1")
print(f"For the test input there are {locate_paper(t1, output=True)[0]} rolls of paper that can be moved")
print(f"For the puzzle input there are {locate_paper(p1)[0]} rolls of paper that can be moved")

print("\nTask 2")
print(f"For the test input there are a {determine_total_to_remove(t1)} total of rolls of paper that can be moved")
print(f"For the puzzle input there are a {determine_total_to_remove(p1)} total of rolls of paper that can be moved")
