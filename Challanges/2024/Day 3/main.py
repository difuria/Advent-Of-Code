from Inputs.puzzle import puzzle_input_1
from Inputs.test import test_input_1, test_input_2

import re

def get_total(puzzle_input, regex):
    muls = re.findall(regex, puzzle_input)
    total = 0
    do = True
    for mul in muls:
        if mul == "do()":
            do = True
            continue
        elif mul == "don't()":
            do = False
            continue
        elif not do:
            continue

        mul = mul.replace("mul(", "").replace(")", "")
        x, y = list(map(int, mul.split(",")))
        total += (x*y)
    
    return total

regex = r'mul\([0-9]{1,},[0-9]{1,}\)'
print(f"Total for test input is {get_total(test_input_1, regex)}")
print(f"Total for puzzle input is {get_total(puzzle_input_1, regex)}")

regex = r'(mul\([0-9]{1,},[0-9]{1,}\)|don\'t\(\)|do\(\))'
print(f"Total for task 2 test input 1 is {get_total(test_input_1, regex)}")
print(f"Total for task 2 test input 2 is {get_total(test_input_2, regex)}")
print(f"Total for task 2 puzzle input is {get_total(puzzle_input_1, regex)}")