from Inputs.puzzle_inputs import puzzle_input_1
from Inputs.test_inputs import test_input_1, test_input_2

import re

def is_string_nice(string: str) -> bool:
    if re.search(r"(ab|cd|pq|xy)", string):
        return False

    vowels = re.findall(r"[aeiou]", string)
    if len(vowels) < 3:
        return False
    
    if not re.search(r"(.)\1", string):
        return False
    
    return True


def is_string_nice_2(string: str) -> bool:
    if not re.search(r"(..).*\1", string):
        return False
    elif not re.search(r"(.).\1", string):
        return False
    
    return True


def count_nice_strings(strings: str, task: int = 1):
    strings = strings.strip().split("\n")

    nice_strings = 0
    for string in strings:

        if (task == 1 and is_string_nice(string)) or (task == 2 and is_string_nice_2(string)):
            nice_strings += 1
    
    print(f"There are {nice_strings} nice strings.")

print("Task 1")
count_nice_strings(test_input_1)
count_nice_strings(puzzle_input_1)

print("\nTask 2")
count_nice_strings(test_input_2, 2)
count_nice_strings(puzzle_input_1, 2)