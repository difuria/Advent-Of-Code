import os, sys

def get_file(path, file):
    file = os.path.join(path, f"Task Inputs", file)

    if not os.path.exists(file):
        print(f"Invalid file supplied of {file}")
        sys.exit(1)

    with open(file, "r") as f:
        path_info = f.read()

    return path_info

def sort_passphrases(passphrases):
    for i, passphrase in enumerate(passphrases):
        p = []
        for item in passphrase.split():
            item = "".join(sorted(list(item)))
            p.append(item)
        passphrases[i] = " ".join(p)

    return passphrases

def count_valid_passphrases(passphrases):
    valid_passphrases = 0
    for passphrase in passphrases:
        passphrase_list = passphrase.split()
        passphrase_set = set(passphrase_list)
        if len(passphrase_set) == len(passphrase_list):
            valid_passphrases += 1
        
    print(f"There were {valid_passphrases} passphrases.")
    
if __name__ == "__main__":
    path = os.path.dirname(__file__)
    test_passphrases_1 = get_file(path, "test_passphrases_1.txt").strip().splitlines()
    test_passphrases_2 = get_file(path, "test_passphrases_2.txt").strip().splitlines()
    puzzle_passphrases = get_file(path, "puzzle_passphrases_1.txt").strip().splitlines()

    print("Task 1")
    print("Test Inputs")
    count_valid_passphrases(test_passphrases_1)

    print("Puzzle Inputs")
    count_valid_passphrases(puzzle_passphrases)

    print("\nTask 2")
    print("Test Inputs")
    count_valid_passphrases(sort_passphrases(test_passphrases_2))

    print("Puzzle Inputs")
    count_valid_passphrases(sort_passphrases(puzzle_passphrases))
