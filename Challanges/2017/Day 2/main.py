import os, sys

def get_file(path, file):
    file = os.path.join(path, f"Task Inputs", file)

    if not os.path.exists(file):
        print(f"Invalid file supplied of {file}")
        sys.exit(1)

    with open(file, "r") as f:
        path_info = f.read()

    return path_info

def find_check_sum(spreadsheet):
    total = 0
    for line in spreadsheet.strip().splitlines():
        line = list(map(int, line.split()))
        total += max(line) - min(line)
    
    print(f"Check sum is {total}.")

def find_evenly_divided(spreadsheet):
    total = 0
    for line in spreadsheet.strip().splitlines():
        line = list(map(int, line.split()))
        line.sort()

        current_index = len(line) - 1
        while current_index >= 1:
            for i in range(0, current_index):
                if line[current_index] % line[i] == 0:
                    total += (line[current_index] // line[i])
                    current_index = -1
                    break
            current_index -= 1
    
    print(f"Divisible total is {total}.")

if __name__ == "__main__":
    path = os.path.dirname(__file__)

    print("Test task:")
    find_check_sum(get_file(path, f"test_spreadsheet_1.txt"))
    find_evenly_divided(get_file(path, f"test_spreadsheet_2.txt"))
    print("\n Puzzle Task:")
    spreadsheet = get_file(path, f"puzzle_spreadsheet_1.txt")
    find_check_sum(spreadsheet)
    find_evenly_divided(spreadsheet)
