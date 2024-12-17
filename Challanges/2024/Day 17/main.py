from Inputs.test_inputs import test_input_1

import re


def get_debugger(text: str) -> dict[str, int]:
    debugger = {}
    registers = re.findall(r"Register\s{1,}(A|B|C):\s{1}(\d{1,})", text)

    for register in registers:
        debugger[register[0]] = register[1]

    program = text.strip().splitlines()[-1]
    p, v = program.split(":")

    debugger[p] = list(map(int, v.strip().split(",")))

    return debugger