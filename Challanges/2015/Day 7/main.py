from Inputs.test_inputs import test_input_1
from Inputs.puzzle_inputs import puzzle_input_1

values: dict[str, str] = {}

def load_values():
    for command in puzzle_input_1.strip().splitlines():
        _input, _output = command.split("->")
        _input = _input.strip()
        _output = _output.strip()

        if _input.isdigit():
            values[_output] = int(_input)
        else:
            values[_output] = _input.split()

def solve(val: str):
    if isinstance(val, int):
        return val
    elif val.strip().isdigit():
        return int(val)
    elif isinstance(values[val], int):
        return values[val]

    if len(values[val]) == 1:
        values[val] = solve(values[val][0])
    elif values[val][1] == "AND":
        values[val] = solve(values[val][0]) & solve(values[val][2])
    elif values[val][1] == "OR":
        values[val] = solve(values[val][0]) | solve(values[val][2])
    elif values[val][0] == "NOT":
        values[val] = 65535 - solve(values[val][1])
    elif values[val][1] == "LSHIFT":
        values[val] = solve(values[val][0]) << solve(values[val][2])
    elif values[val][1] == "RSHIFT":
        values[val] = solve(values[val][0]) >> solve(values[val][2])
    else:
        raise RuntimeError(f"Unknown: {values[val]}")

    return values[val]

load_values()
print("Value for a is", solve("a"))

a: int = solve("a")
load_values()
values["b"] = a
print("Value for a is now", solve("a"))