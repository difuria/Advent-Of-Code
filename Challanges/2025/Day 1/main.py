from Inputs.test import test1
from Inputs.puzzle import puzzle1

def read_combination(combinations: str, start: int = 50) -> int:
    combos: list[str] = combinations.strip().splitlines()
    current: int = start
    zero_count: int = 0

    for combo in combos:
        direction: str = combo[0]
        value: int = int(combo[1:])

        if direction == "L":
            current -= value
        else:
            current += value

        if current < 0:
            if (abs(current) % 100) == 0:
                current = 0
            else:
                current = 100 - (abs(current) % 100)
        elif current > 99:
            current = 0 + (abs(current) % 100)

        if current == 0:
            zero_count += 1

    return zero_count

print("Part 1")
print(f"Test 0's: {read_combination(test1)}")
print(f"Puzzle 0's: {read_combination(puzzle1)}")