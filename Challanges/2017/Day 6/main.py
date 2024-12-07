from Inputs.puzzle_inputs import puzzle_inputs_1
from Inputs.test_inputs import test_input_1, test_input_2

import sys

def redistribution_cycles(text: str, task: int = 1) -> None:
    seen_banks: list = []
    bank = list(map(int, text.strip().split()))
    bank_length = len(bank)

    redistribution_count = 0
    while bank not in seen_banks:
        if task == 1 or (task == 2 and len(seen_banks) == 0):
            seen_banks.append(bank[:])
            # print("Adding bank", seen_banks)

        max_item = -sys.maxsize - 1
        index = -1
        for i, item in enumerate(bank):
            if item > max_item:
                max_item = item
                index = i
        
        bank[index] = 0
        while max_item > 0:
            index += 1
            if index >= bank_length:
                index = 0
            
            bank[index] += 1
            max_item -= 1
        
        redistribution_count += 1

    print(f"Redistribution count is {redistribution_count}.")
    return bank


print("Task 1")
test_bank = redistribution_cycles(test_input_1)
puzzle_bank = redistribution_cycles(puzzle_inputs_1)

print("\nTask 2")
redistribution_cycles(" ".join(list(map(str, test_bank))), 2)
redistribution_cycles(" ".join(list(map(str, puzzle_bank))), 2)