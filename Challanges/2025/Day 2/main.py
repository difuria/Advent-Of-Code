from Inputs.test import test1
from Inputs.puzzle import puzzle1

def invalid_ids(combinations: str) -> int:
    seen: dict[str, int] = {}
    count: int = 0
    for combo in combinations.strip().split(","):
        start, end = combo.split("-")

        for i in range(int(start), int(end)+1):
            cur = str(i)

            if i not in seen:
                cur_count: int = 0
                for j in range(len(cur)):
                    if cur[:j] == cur[j:]:
                        cur_count += i
                seen[i] = cur_count

            count += seen[i]
    
    return count

print("Part 1")
print(f"Invalid test IDs: {invalid_ids(test1)}")
print(f"Invalid puzzle IDs: {invalid_ids(puzzle1)}")