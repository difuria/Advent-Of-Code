import os, sys

input_text = "puzzle_report_1.txt"

class SonarSweep:
    def __init__(self, report):
        self.report = list(map(int, report.strip().split("\n")))

    def __count_increases(self, report):
        count = 0
        for index, line in enumerate(report):
            if index == 0:
                continue
            elif report[index-1] < line:
                count += 1
        
        print(f"Increased {count} times.")

    def number_of_increases(self):
        # Solution to task 1
        self.__count_increases(self.report)

    def number_of_sliding_increases(self, sliding_window=3):
        # Solution to task 2
        sliding_report = []
        
        for index, line in enumerate(self.report):
            end_index = index+sliding_window
            if end_index <= len(self.report):
                sliding_window_sum = sum(self.report[index:end_index])
                sliding_report.append(sliding_window_sum)
        
        self.__count_increases(sliding_report)

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
    sonar_sweep.number_of_sliding_increases()
