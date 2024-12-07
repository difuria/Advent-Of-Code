from Inputs.puzzle_inputs import puzzle_input_1
from Inputs.test_inputs import test_input_1


def get_jumps(text: str) -> list:
    return list(map(int, text.strip().split("\n")))


def count_jumps(jumps: list, task: int = 1) -> None:
    index = 0
    jumps_taken = 0

    while index <= len(jumps)-1:
        jumps_taken += 1
        if jumps[index] == 0:
            jumps[index] += 1
            continue

        old_index = index
        index += jumps[index]

        if task == 2 and jumps[old_index] >= 3:
            jumps[old_index] -= 1
        else:
            jumps[old_index] += 1

    print(f"A total of {jumps_taken} jumps were taken.")


print("Task 1")
jumps = get_jumps(puzzle_input_1)
count_jumps(jumps, 1)

print("\nTask 2")
jumps = get_jumps(puzzle_input_1)
count_jumps(jumps, 2)