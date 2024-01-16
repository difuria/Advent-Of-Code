import os, sys

class Passports:
    def __init__(self, passports):
        passports = [passport.split() for passport in passports.strip().split("\n\n")]
        self.passports = []
        for i, passport in enumerate(passports):
            pp = {}
            for item in passport:
                key, value = item.split(":")
                pp[key] = value
            self.passports.append(pp)

    def check_passports(self):
        valid_count = 0
        for passport in self.passports:
            if len(passport) == 8 or (not "cid" in passport and len(passport) == 7):
                valid_count += 1
            
        print(f"There are {valid_count} valid passports.")

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

    print("Test Passports")
    passports = Passports(get_file(path, "test_batch_file_1.txt"))
    passports.check_passports()

    print("\nPuzzle Passports")
    passports = Passports(get_file(path, "puzzle_batch_file_1.txt"))
    passports.check_passports()
