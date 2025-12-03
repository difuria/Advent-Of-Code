from Inputs.test import t1
from Inputs.puzzle import p1

def get_max(bank: str, start: int, end: int) -> tuple[int]:
    max: int = -1
    pos: int = -1
    for i in range(start, end):
        cur = int(bank[i])
        if cur > max:
            max = cur
            pos = i

    return max, pos

def get_joltage(banks: str, length: int = 2) -> int:
    joltage:int = 0
    for bank in banks.strip().splitlines():
        bank = bank.strip()

        jolt: str = ""
        pos: int = -1
        for remaining_length in range(length-1, -1, -1):
            max, pos = get_max(bank, pos+1, len(bank)-remaining_length)
            jolt += str(max)
        
        joltage += int(jolt)

    return joltage

print("Task 1")
print(f"Test joltage is {get_joltage(t1)}")
print(f"Puzzle joltage is {get_joltage(p1)}")

print("\nTask 2")
print(f"Test joltage is {get_joltage(t1, 12)}")
print(f"Puzzle joltage is {get_joltage(p1, 12)}")