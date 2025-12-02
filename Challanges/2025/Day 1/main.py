from Inputs.test import test1
from Inputs.puzzle import puzzle1

def read_combination(combinations: str, start: int = 50) -> int:
    combos: list[str] = combinations.strip().splitlines()
    current: int = start
    zero_count: int = 0

    for combo in combos:
        direction: str = combo[0]
        clicks: int = int(combo[1:])

        if direction == "L":
            current -= clicks
        else:
            current += clicks

        if (abs(current) % 100) == 0:
            current = 0
        elif current < 0:
            current = 100 - (abs(current) % 100)
        elif current > 99:
            current = 0 + (abs(current) % 100)

        if current == 0:
            zero_count += 1

    return zero_count


def read_all_zeros(combinations: str, start: int = 50) -> int:
    combos: list[str] = combinations.strip().splitlines()
    current: int = start
    zero_count: int = 0

    for combo in combos:
        direction: str = combo[0]
        clicks: int = int(combo[1:])

        if clicks == 0:
            continue  # Only count clicks a clicks of 0 means we haven't moved

        scur:int = current
        zero_count += (clicks // 100)
        clicks = clicks % 100

        if direction == "L":
            current -= clicks
        else:
            current += clicks
        
        if current == 0:
            zero_count += 1
        elif current < 0:
            current += 100
            if scur != 0:
                zero_count += 1
        elif current > 99:
            current -= 100
            zero_count += 1

    return zero_count


print("Part 1")
print(f"Test 0's: {read_combination(test1)}")
print(f"Puzzle 0's: {read_combination(puzzle1)}")

print("\nPart 2")
print(f"{read_all_zeros(test1)}")
print(f"{read_all_zeros(puzzle1)}")