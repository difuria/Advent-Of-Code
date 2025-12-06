from Inputs.test import t1
from Inputs.puzzle import p1


def cephalopod_math(worksheet: str) -> int:
    worksheet_values: list[list[str]] = []

    ws: list[str] = worksheet.strip().splitlines()
    for row in ws[:-1]:
        current: list[int, str] = []
        for col in row.split():
            current.append(int(col))

        worksheet_values.append(current[:])

    worksheet_actions: list[str] = ws[-1].split()

    for col in range(len(worksheet_values[0])):
        for row in range(1, len(worksheet_values)):
            if worksheet_actions[col] == "+":
                worksheet_values[row][col] = worksheet_values[row][col] + worksheet_values[row-1][col]
            elif worksheet_actions[col] == "*":
                worksheet_values[row][col] = worksheet_values[row][col] * worksheet_values[row-1][col]

    anwser: int = 0
    for col in range(len(worksheet_values[0])):
        anwser += worksheet_values[-1][col]

    return anwser


def cephalopod_math_2(worksheet: str) -> int:
    ws: list[str] = worksheet.splitlines()

    # It also depends if the numbers are left or right aligned
    # Easiest way I can tell how to seperate the integers is based on the operators
    # Which all seem to be left aligned 
    # Distances could also be different each time so determine what the differences are

    distances: list[int] = []
    last_found_index: int = 0

    for i in range(1, len(ws[-1])):
        if ws[-1][i] != " ":
            distances.append(i-last_found_index)  # This distance includes a space so will need to be dealt with later
            last_found_index = i

    distances.append(i-last_found_index+2) # Add a fictional last whitespace for the final one to make it easier to deal with
    
    worksheet_actions: list[str] = ws[-1].split()
    current_offset: int = 0
    answer: int = 0
    for col in range(len(distances)):
        values: list[str] = []
        for index in range(current_offset, current_offset + distances[col]-1): # -1 removes the whitespace at the end
            values.append("")
            for row in range(0, len(ws)-1):
                if ws[row][index].isdigit():
                    values[-1] += ws[row][index]

        current_offset += distances[col]

        for val in range(1, len(values)):
            if worksheet_actions[col] == "+":
                values[val] = int(values[val]) + int(values[val-1])
            elif  worksheet_actions[col] == "*":
                values[val] = int(values[val]) * int(values[val-1])

        answer += values[-1]

    return answer

print("Task 1:")
print(f"Test total is: {cephalopod_math(t1)}")
print(f"Puzzle total is: {cephalopod_math(p1)}")

print("\nTask 2:")
print(f"Test total 2 is: {cephalopod_math_2(t1)}")
print(f"Puzzle total 2 is: {cephalopod_math_2(p1)}")
