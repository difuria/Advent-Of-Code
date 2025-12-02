from Inputs.test import test1
from Inputs.puzzle import puzzle1
import re

def invalid_ids(combinations: str) -> int:
    count: int = 0
    for combo in combinations.strip().split(","):
        start, end = combo.split("-")

        for i in range(int(start), int(end)+1):
            cur = str(i)
            if cur[:len(cur)//2] == cur[len(cur)//2:]:
                count += i
    
    return count

def invalid_ids_2(combinations: str) -> int:
    count: int = 0
    for combo in combinations.strip().split(","):
        start, end = combo.split("-")

        for i in range(int(start), int(end)+1):
            cur = str(i)
            for j in range(1, len(cur)):
                if len(cur) % j != 0 or j > (len(cur)//2):  # It won't repeat as the string repeated won't fit in the total string or we're over half way
                    continue 

                if re.search("^(" +  cur[:j] +"){2,}$", cur):
                    count += i
                    break
    
    return count

                

print("Part 1")
print(f"Invalid test IDs: {invalid_ids(test1)}")
print(f"Invalid puzzle IDs: {invalid_ids(puzzle1)}")

print("\nPart 2")
print(f"Invalid test IDs: {invalid_ids_2(test1)}")
print(f"Invalid puzzle IDs: {invalid_ids_2(puzzle1)}")