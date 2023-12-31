import os, re, sys

input_text = "puzzle_records_1.txt"

class HotSprings:
    def __init__(self, records):
        self.records = [r.split() for r in records.strip().split("\n")]

    def create_configurations(self, conditions, regex):
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

                    # We might as well not add if this isn't going to go any further
                    if re.search(regex, "".join(condition_1)):
                        conditions.append(condition_1)
                    if re.search(regex, "".join(condition_2)):
                        conditions.append(condition_2)

                    wild_card_found = True
                    break
            if not wild_card_found:
                cond = "".join(condition)
                if re.search(regex, cond):
                    full_conditions.append(cond)

        return full_conditions

    def determine_valid_configuration(self, repeat = 1):
        # TODO fix - For task 2 it takes ages to run
        total_count = 0
        for r in self.records:
            
            condition, record = r
            record = record.split(",")

            regex = []
            for r in record:
                regex.append(f"(#|\?){{{r}}}")
                regex.append(r"(\.|\?){1,}")

            regex = r"^(\.|\?){0,}" + "".join((regex * repeat)[:-1]) + r"(\.|\?){0,}$"

            cond = ""
            for i in range(repeat):
                cond += condition + "?" 
            print(f"Searching:{cond[:-1]}\n{regex}")
            conditions = self.create_configurations([list(cond[:-1])], regex)

            print(f"Valid Conditions: {len(conditions)}")
            total_count += len(conditions)

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
