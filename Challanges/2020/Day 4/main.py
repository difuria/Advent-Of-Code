import os, re, sys

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

    def check_passports(self, with_conditions=False):
        valid_count = 0
        for passport in self.passports:
            if len(passport) == 8 or (not "cid" in passport and len(passport) == 7):
                valid_count += 1
            
        print(f"There are {valid_count} valid passports.")

        if with_conditions:
            valid_count = 0
            for passport in self.passports:
                currently_valid = True
                for key, value in passport.items():
                    if key == 'byr':
                        if not re.search(r"^(19[2-9][0-9]|200[0-2])$", value):
                            currently_valid = False
                            break
                    elif key == "iyr":
                        if not re.search(r"^20(1[0-9]|20)$", value):
                            currently_valid = False
                            break
                    elif key == "eyr":
                        if not re.search(r"^20(2[0-9]|30)$", value):
                            currently_valid = False
                            break
                    elif key == "hgt":
                        if not re.search(r"^(1([5-8][0-9]|9[0-3])cm|(59|6[0-9]|7[0-6])in)$", value):
                            currently_valid = False
                            break
                    elif key == "hcl":
                        if not re.search(r"^#[0-9a-f]{6}$", value):
                            currently_valid = False
                            break
                    elif key == "ecl":
                        if not value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                            currently_valid = False
                            break
                    elif key == "pid":
                        if not re.search(r"^[0-9]{9}$", value):
                            currently_valid = False
                            break
                    elif key != "cid":
                        currently_valid = False
                        break

                sorted_keys = sorted(passport.keys())
                if sorted_keys != ['byr', 'cid', 'ecl', 'eyr', 'hcl', 'hgt', 'iyr', 'pid'] and \
                   sorted_keys != ['byr', 'ecl', 'eyr', 'hcl', 'hgt', 'iyr', 'pid']:
                    currently_valid = False

                if currently_valid:
                    valid_count += 1

            print(f"Checking conditions there are {valid_count} valid passports.")

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
    passports.check_passports(True)
    passports = Passports(get_file(path, "test_batch_file_2.txt"))
    passports.check_passports(True)
    passports = Passports(get_file(path, "test_batch_file_3.txt"))
    passports.check_passports(True)

    print("\nPuzzle Passports")
    passports = Passports(get_file(path, "puzzle_batch_file_1.txt"))
    passports.check_passports(True)
