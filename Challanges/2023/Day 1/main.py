import os, re, sys

input_text = "puzzle_input_part_2.txt"

class Trebuchet:
    def __init__(self, calibration_document) -> None:
        self.calibration_document = calibration_document.strip()
        self.calibration_values = []

        
        self.digits_to_value = {
            "one": "1",
            "two": "2",
            "three": "3",
            "four": "4",
            "five": "5",
            "six": "6",
            "seven": "7",
            "eight": "8", 
            "nine": "9"
        }
        self.digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.digits = "|".join(list(self.digits_to_value.keys()) + self.digits) 

    def find_values(self):
        for line in self.calibration_document.strip().split("\n"):
            first_digit = self.find_first(line)
            last_digit = self.find_last(line)
            self.calibration_values.append(int(first_digit + last_digit))

    def find_character(self, line, digits):
        digit = re.search(rf"({digits})", line)
        if digit:
            value = digit.group()
            if value in self.digits_to_value:
                return self.digits_to_value[value]
            elif value[::-1] in self.digits_to_value:
                return self.digits_to_value[value[::-1]]
            else:
                return value

    def find_first(self, line):
        return self.find_character(line, self.digits)

    def find_last(self, line):
        return self.find_character(line[::-1], self.digits[::-1])

    def sum_values(self):
        return sum(self.calibration_values)

if __name__ == "__main__":
    path = os.path.dirname(__file__)
    file = os.path.join(path, input_text)

    if not os.path.exists(file):
        print(f"Invalid file supplied of {input_text}")
        sys.exit(1)

    with open(file, "r") as f:
        document = f.read()

    trebuchet = Trebuchet(document)
    trebuchet.find_values()
    print(trebuchet.sum_values())