import os, sys

input_text = "puzzle_report_1.txt"

class BinaryDiagnostic():
    def __init__(self, report) -> None:
        self.report = report.strip().split("\n")

    def calculate_power_consumption(self):
        count = {}
        gamma_binary = ""
        epsilon_binary = ""

        for row in self.report:
            for col_index, col_item in enumerate(row):
                if not col_index in count.keys():
                    count[col_index] = { "0": 0, "1": 0 }
                count[col_index][col_item] += 1

        for column in sorted(count.keys()):
            if count[column]["0"] > count[column]["1"]:
                gamma_binary += "0"
                epsilon_binary += "1"
            elif count[column]["0"] < count[column]["1"]:
                gamma_binary += "1"
                epsilon_binary += "0"

        gamma_rate = int(gamma_binary, 2)
        epsilon_rate = int(epsilon_binary, 2)
        power_consumption = gamma_rate * epsilon_rate
        print(f"Gamma rate is {gamma_binary} or {gamma_rate} in decimal.")
        print(f"Epsilon rate is {epsilon_binary} or {epsilon_rate} in decimal.")
        print(f"Power consumption if {power_consumption}")
    
    def verify_life_support_rating(self):
        oxygen_generator_numbers = self.report[:]
        column = 0
        while oxygen_generator_numbers:
            start_with_one = []
            start_with_zero = []
            for number in oxygen_generator_numbers:
                if number[column] == "1":
                    start_with_one.append(number)
                else:
                    start_with_zero.append(number)
            
            if len(start_with_one) > len(start_with_zero):
                oxygen_generator_numbers = start_with_one[:]
            elif len(start_with_one) < len(start_with_zero):
                oxygen_generator_numbers = start_with_zero[:]
            else:
                oxygen_generator_numbers = [number for number in oxygen_generator_numbers if number[column] == "1"]

            if len(oxygen_generator_numbers) == 1:
                break

            column += 1       

        co2_scrubber_numbers = self.report[:]
        column = 0
        while co2_scrubber_numbers:
            start_with_one = []
            start_with_zero = []
            for number in co2_scrubber_numbers:
                if number[column] == "1":
                    start_with_one.append(number)
                else:
                    start_with_zero.append(number)
            
            if len(start_with_one) < len(start_with_zero):
                co2_scrubber_numbers = start_with_one[:]
            elif len(start_with_one) > len(start_with_zero):
                co2_scrubber_numbers = start_with_zero[:]
            else:
                co2_scrubber_numbers = [number for number in co2_scrubber_numbers if number[column] == "0"]

            if len(co2_scrubber_numbers) == 1:
                break

            column += 1 

        oxygen_generator_rating = int(oxygen_generator_numbers[0], 2)
        co2_scrubber_rating = int(co2_scrubber_numbers[0], 2)
        life_support_rating = oxygen_generator_rating * co2_scrubber_rating
        print(f"Oxygen generator rating is {oxygen_generator_numbers[0]}, or in decimal {oxygen_generator_rating}")     
        print(f"Co2 Scrubber rating is {co2_scrubber_numbers[0]}, or in decimal {co2_scrubber_rating}")
        print(f"Lif support rating is {life_support_rating}")

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

    binary_diagnostic = BinaryDiagnostic(get_file(path, input_text))
    binary_diagnostic.calculate_power_consumption()
    binary_diagnostic.verify_life_support_rating()