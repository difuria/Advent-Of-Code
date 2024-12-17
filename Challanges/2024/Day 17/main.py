from Inputs.puzzle_inputs import puzzle_input_1
from Inputs.test_inputs import test_input_1

import re


def get_debugger(text: str) -> dict[str, int]:
    debugger = { "out": [] }
    registers = re.findall(r"Register\s{1,}(A|B|C):\s{1}(\d{1,})", text)

    for register in registers:
        debugger[register[0]] = int(register[1])

    program = text.strip().splitlines()[-1]
    p, v = program.split(":")

    debugger[p] = list(map(int, v.strip().split(",")))

    return debugger


def get_combo_operand(debugger: dict[str, int], operand: int) -> int:
        if operand == 7:
            raise ValueError("7 Should not appear in a valid program")

        combo_operand = {
            4: debugger["A"],
            5: debugger["B"],
            6: debugger["C"],
        }

        return combo_operand.get(operand, operand)


def dv(debugger: dict[str, int], operand: int) -> int:
    numerator = debugger["A"]
    denominator = 2**get_combo_operand(debugger, operand)
    return int(numerator / denominator)


def execute_opcode(opcode: int, operand: int, debugger: dict[str, int]) -> dict[str, int]:
    if opcode == 0:
        # adv
        debugger["A"] = dv(debugger, operand)
    elif opcode == 1:
        # bxl
        debugger["B"] = debugger["B"] ^ operand
    elif opcode == 2:
        # bst
        modulo = get_combo_operand(debugger, operand) % 8
        print("Modulo", modulo)
        debugger["B"] = get_combo_operand(debugger, operand) % 8
    elif opcode == 3:
        # jnz
        if debugger["A"] == 0:
            # Do nothing
            return debugger
        # Needs to recursively call
        return execute_opcode(operand, operand, debugger)
    elif opcode == 4:
        # bxc
        debugger["B"] =  debugger["B"] ^ debugger["C"]
    elif opcode == 5:
        # out
        modulo = get_combo_operand(debugger, operand) % 8
        debugger["out"] += list(str(modulo))
    elif opcode == 6:
        # bdv
        debugger["B"] = dv(debugger, operand)
    elif opcode == 7:
        # cdv
        debugger["C"] = dv(debugger, operand)
    else:
        raise ValueError(f"Invalid opcode of {opcode} supplied.")

    return debugger


def run_program(debugger: dict[str, int]) -> None:
    for i in range(0, len(debugger["Program"]), 2):
        opcode = debugger["Program"][i]
        operand = debugger["Program"][i+1]

        debugger = execute_opcode(opcode, operand, debugger)
    
    print(debugger)
    input()
    return debugger


_debugger = get_debugger(puzzle_input_1)
print(_debugger)
while len(_debugger["out"]) == 0 or _debugger["out"][-1] != '0':
    _debugger = run_program(_debugger)

print("output: " + ",".join(_debugger["out"]))