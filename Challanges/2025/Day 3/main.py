from Inputs.test import t1
from Inputs.puzzle import p1

def get_max(bank: str) -> tuple[int]:
    max: int = -1
    pos: int = -1
    for i, cur in enumerate(bank):
        if int(cur) > max:
            max = int(cur)
            pos = i
    
    return max, pos

def get_joltage(banks: str) -> int:
    joltage:int = 0
    for bank in banks.strip().splitlines():
        bank = bank.strip()

        max, fpos = get_max(bank[:-1])
        sec, spos = get_max(bank[fpos+1:])
        
        joltage += int(str(max) + str(sec))

    
    return joltage

print("Task 1")
print(f"Test joltage is {get_joltage(t1)}")
print(f"Puzzle joltage is {get_joltage(p1)}")
