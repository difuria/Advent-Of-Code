import os
import sys

def is_safe(levels: list) -> bool:
    if levels[0] > levels[1]:
        increasing = False
    elif levels[0] < levels[1]:
        increasing = True
    else:
        return False

    for i in range(len(levels)-1):
        if not increasing and levels[i] <= levels[i+1]:
            return False
        elif increasing and levels[i] >= levels[i+1]:
            return False
        elif abs(levels[i] - levels[i+1]) > 3:
            return False
    
    return True

def get_file(path: str, file: str) -> str:
    file = os.path.join(path, f"Task Inputs", file)

    if not os.path.exists(file):
        print(f"Invalid file supplied of {file}")
        sys.exit(1)

    with open(file, "r") as f:
        path_info = f.read()

    return path_info

if __name__ == "__main__":
    path = os.path.dirname(__file__)

    input_reports = get_file(path, "puzzle_input_1.txt").strip().split("\n")

    safe_reports = 0
    for report in input_reports:
        levels = list(map(int, report.strip().split()))

        if is_safe(levels):
            safe_reports += 1
    
    print(f"There are {safe_reports} safe reports (puzzle 1).")

    safe_reports = 0
    for report in input_reports:
        levels = list(map(int, report.strip().split()))

        safe = False
        for i in range(len(levels)):
            current_levels = levels[:]
            current_levels.pop(i)
            safe = is_safe(current_levels)
            if safe:
                break

        if safe:
            safe_reports += 1

    print(f"There are {safe_reports} safe reports (puzzle 2).")