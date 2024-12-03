from Inputs.puzzle import puzzle_input_1
from Inputs.test import test_input_1, test_input_2

import re

def get_total(puzzle_input):
    muls = re.findall(r'mul\([0-9{1,},[0-9]{1,}\)', puzzle_input)
    total = 0
    for mul in muls:
        mul = mul.replace("mul(", "").replace(")", "")
        try:
            x, y = list(map(int, mul.split(",")))
            total += (x*y)
        except:
            # Ignore single finds such as mul(901)
            pass
    
    return total

print(f"Total for test input is {get_total(test_input_1)}")
print(f"Total for puzzle input is {get_total(puzzle_input_1)}")

def get_total_2(puzzle_input):
    muls = re.findall(r'(mul\([0-9{1,},[0-9]{1,}\)|don\'t\(\)|do\(\))', puzzle_input)
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
        try:
            x, y = list(map(int, mul.split(",")))
            total += (x*y)
        except:
            # Ignore single finds such as mul(901)
            pass
    
    return total

print(f"Total for task 2 test input 1 is {get_total_2(test_input_1)}")
print(f"Total for task 2 test input 2 is {get_total_2(test_input_2)}")
print(f"Total for task 2 puzzle input is {get_total_2(puzzle_input_1)}")