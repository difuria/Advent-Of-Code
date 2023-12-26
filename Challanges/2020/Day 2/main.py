import os, sys

input_text = "puzzle_passwords_1.txt"

class PasswordPhilosophy:
    def __init__(self, passwords):
        self.passwords = passwords.strip().split("\n")
    
    def count_valid_passwords(self):
        valid = 0
        for line in self.passwords:
            range, letter, password = line.split()
            lower_value, upper_value = list(map(int, range.split("-")))
            letter = letter.replace(":", "")

            letter_occurrence = password.count(letter)
            if lower_value <= letter_occurrence <= upper_value:
                valid += 1

        print(f"{valid} passwords are valid.")
    
    def count_valid_locations(self):
        valid = 0
        for line in self.passwords:
            range, letter, password = line.split()
            first_value, second_value = list(map(int, range.split("-")))
            letter = letter.replace(":", "")
            
            if (password[first_value-1] == letter or password[second_value-1] == letter) and \
                not (password[first_value-1] == letter and password[second_value-1] == letter) :
                valid += 1

        print(f"{valid} passwords are valid.")

if __name__ == "__main__":
    path = os.path.dirname(__file__)
    file = os.path.join(path, input_text)

    if not os.path.exists(file):
        print(f"Invalid file supplied of {input_text}")
        sys.exit(1)

    with open(file, "r") as f:
        passwords = f.read()

    password_philosophy = PasswordPhilosophy(passwords)
    password_philosophy.count_valid_passwords()
    password_philosophy.count_valid_locations()
