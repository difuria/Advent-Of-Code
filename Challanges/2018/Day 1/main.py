import os, sys

input_text = "test_frequency_1.txt"

def get_file(path, file):
    file = os.path.join(path, f"Task Inputs", file)

    if not os.path.exists(file):
        print(f"Invalid file supplied of {file}")
        sys.exit(1)

    with open(file, "r") as f:
        path_info = f.read()

    return path_info

if __name__ == "__main__":
    path = os.path.dirname(__file__)

    frequencies = get_file(path, input_text).strip().split()

    print("Task 1")
    for i in range(1, 5):
        frequencies = get_file(path, f"test_frequency_{i}.txt").strip().split()
        duplicate = set()
        first_duplicate = None
        resulting_frequency = 0
        for frequency in frequencies:
            resulting_frequency += int(frequency)
        
        print(f"Resulting frequency of {resulting_frequency}.")

    frequencies = get_file(path, f"puzzle_frequency_1.txt").strip().split()
    resulting_frequency = 0
    for frequency in frequencies:
        resulting_frequency += int(frequency)
    
    print(f"Resulting frequency of {resulting_frequency}.")

    print("\nTask 2")
    for i in range(5, 9):
        frequencies = get_file(path, f"test_frequency_{i}.txt").strip().split()
        duplicate = { 0 }
        first_duplicate = None
        resulting_frequency = 0
        while first_duplicate == None:
            for frequency in frequencies:
                resulting_frequency += int(frequency)
                if resulting_frequency in duplicate:
                    first_duplicate = resulting_frequency
                    break
                duplicate.add(resulting_frequency)

        print(f"First Duplicate is {resulting_frequency}")

    frequencies = get_file(path, f"puzzle_frequency_1.txt").strip().split()
    duplicate = { 0 }
    first_duplicate = None
    resulting_frequency = 0
    while first_duplicate == None:
        for frequency in frequencies:
            resulting_frequency += int(frequency)
            if resulting_frequency in duplicate:
                first_duplicate = resulting_frequency
                break
            duplicate.add(resulting_frequency)
    
    print(f"First Duplicate is {resulting_frequency}")