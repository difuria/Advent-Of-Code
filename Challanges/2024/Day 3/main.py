from Inputs.puzzle import puzzle_input_1
from Inputs.test import test_input_1, test_input_2

import re

def get_total(puzzle_input, regex):
    do = True
    muls = re.findall(regex, puzzle_input)
    total = 0
    for mul in muls:
        if re.search(r"do(n't|)\(\)", mul[0]):
            do = True if mul[0] == "do()" else False
            continue
        elif not do:
            continue

        total += (int(mul[-2])*int(mul[-1]))
    
    return total

regex = r'mul\((\d{1,}),(\d{1,})\)'
print("Task 1")
print(f"Total for test input is {get_total(test_input_1, regex)}")
print(f"Total for puzzle input is {get_total(puzzle_input_1, regex)}")

regex = r'(mul\((\d{1,}),(\d{1,})\)|don\'t\(\)|do\(\))'
print("\nTask 2")
print(f"Total test input 1 is {get_total(test_input_1, regex)}")
print(f"Total test input 2 is {get_total(test_input_2, regex)}")
print(f"Total puzzle input is {get_total(puzzle_input_1, regex)}")