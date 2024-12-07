from Inputs.puzzle_inputs import puzzle_input_1
from Inputs.test_inputs import test_input_1, test_input_2

def get_equations(text: str) -> list:
    text_split = text.strip().split("\n")

    equations: list = []
    for line in text_split:
        answer, values = line.strip().split(":")
        answer = int(answer)
        values = list(map(int, values.split()))

        equations.append([answer, values])
    
    return equations


def is_valid_equation(equation: list, task: int = 1) -> bool:
    operators: list = ["+", "*"]
    if task == 2:
        operators.append("||")

    values = equation[1]

    potential_equations: list = []
    value = values.pop(0)
    potential_equations.append([value])

    # Produce a list of all the possible equations a list could produce 
    while values:
        value = values.pop(0)

        current_equations = potential_equations[:]
        potential_equations = []
        while current_equations:
            current_equation = current_equations.pop(0)

            for operator in operators:
                current = current_equation[:]
                current.append(operator)
                current.append(value)
                potential_equations.append(current)

    for eq in potential_equations:
        value = eq[0]
        for i in range(1, len(eq), 2):
            if eq[i] == "+":
                value += eq[i+1]
            elif eq[i] == "*":
                value *= eq[i+1]
            elif eq[i] == "||":
                value = int(str(value) + str(eq[i+1]))
            else:
                raise ValueError(f"Unknown operator of {eq[i]} in {eq}")

        if value == equation[0]:
            return True

    return False


def sum_valid_equations(equations: list, task: int = 1) -> None:
    total = 0
    for equation in equations:
        if is_valid_equation(equation, task):
            total += equation[0]
    
    print(f"The total for the valid equations is {total}.")


print(f"Task 1")
equations = get_equations(puzzle_input_1)
sum_valid_equations(equations)

print(f"\nTask 2")
equations = get_equations(puzzle_input_1)
sum_valid_equations(equations, 2)