import os, re, sys

input_text = "puzzle_records_1.txt"

class HotSprings:
    def __init__(self, records):
        self.records = [r.split() for r in records.strip().split("\n")]

    def create_configurations(self, conditions = []):
        full_conditions = []
        while conditions:
            condition = conditions.pop(0)
            wild_card_found = False
            for i, character in enumerate(condition):
                if character == "?":
                    condition_1 = condition[:]
                    condition_1[i] = "."
                    condition_2 = condition[:]
                    condition_2[i] = "#"

                    conditions.append(condition_1)
                    conditions.append(condition_2)

                    wild_card_found = True
                    break
            if not wild_card_found:
                full_conditions.append("".join(condition))
        
        return full_conditions

    def determine_valid_configuration(self):
        total_count = 0
        for r in self.records:
            condition, record = r
            record = record.split(",")
            conditions = self.create_configurations([list(condition)])

            regex = [r"^\.{0,}"]
            for r in record:
                regex.append(f"#{{{r}}}")
                regex.append(r"\.{1,}")
            
            regex = "".join(regex[:-1]) + r"\.{0,}$"

            valid_count = 0
            for c in conditions:
                if re.search(regex, c):
                    valid_count += 1

            total_count += valid_count

        print(f"Total count is {total_count}")

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

    hot_springs = HotSprings(get_file(path, input_text))
    hot_springs.determine_valid_configuration()
