import os, sys

input_text = "test_report_1.txt"

class SonarSweep:
    def __init__(self, report):
        self.report = list(map(int, report.strip().split("\n")))
    
    def number_of_increases(self):
        # Solution to task 1
        count = 0
        for index, line in enumerate(self.report):
            if index == 0:
                continue
            elif self.report[index-1] < line:
                count += 1
        
        print(f"Increased {count} times.")

if __name__ == "__main__":
    path = os.path.dirname(__file__)
    file = os.path.join(path, input_text)

    if not os.path.exists(file):
        print(f"Invalid file supplied of {input_text}")
        sys.exit(1)

    print(file)
    with open(file, "r") as f:
        report = f.read()

    sonar_sweep = SonarSweep(report)
    sonar_sweep.number_of_increases()
