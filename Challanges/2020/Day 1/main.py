import os, sys

input_text = "puzzle_report_1.txt"

class ReportRepair:
    def __init__(self, report):
        self.report = list(map(int, report.strip().split("\n")))

    def repair(self, sum = 2020):
        # Solution to part 1
        current_entries = set()
        for value in self.report:
            other_value = sum - value
            if other_value in current_entries:
                return other_value * value
            current_entries.add(value)
    
    def repair_3(self, sum = 2020):
        # Solution to part 2
        current_entries = set()
        for first_value in self.report:
            for second_value in current_entries:
                third_value = sum - first_value - second_value
                if third_value in current_entries:
                    return first_value * second_value * third_value
            current_entries.add(first_value)

if __name__ == "__main__":
    path = os.path.dirname(__file__)
    file = os.path.join(path, input_text)

    if not os.path.exists(file):
        print(f"Invalid file supplied of {input_text}")
        sys.exit(1)

    with open(file, "r") as f:
        report = f.read()

    report_repair = ReportRepair(report)
    print(report_repair.repair())
    print(report_repair.repair_3())
