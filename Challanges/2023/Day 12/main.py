import os, re, sys

input_text = "puzzle_records_1.txt"

class HotSprings:
    def __init__(self, records):
        self.records = [r.split() for r in records.strip().split("\n")]

    def create_configurations(self, conditions, regex):
        full_conditions = []
        starting_index = 0
        while conditions:
            condition = conditions.pop(0)
            wild_card_found = False
            for i in range(starting_index, len(condition)):
                character = condition[i]
                if character == "?":
                    starting_index = i
                    condition_1 = condition[:]
                    condition_1[i] = "."
                    condition_2 = condition[:]
                    condition_2[i] = "#"

                    # Don't add if this isn't going to go any further
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

            regex = [f"(#|\?){{{r}}}" for r in record]
            regex = r"^(\.|\?){0,}" + r"(\.|\?){1,}".join((regex * repeat)) + r"(\.|\?){0,}$"

            condition = "?".join([condition] * repeat) 
            print(f"Searching:{condition}")
            condition = re.sub(r"\.{2,}", ".", condition) # We can remove unnecessary .'s
            condition = re.sub(r"(^\.|\.$)", "", condition)
            conditions = self.create_configurations([list(condition)], regex)

            print(f"Valid Conditions: {len(conditions)}")
            total_count += len(conditions)

        print(f"Total count is {total_count}")

    def recursive_count(self, condition, record):
        if condition == "" :
            # If nothing is remainig and no records match 
            return 1 if record == () else 0

        if record == ():
            return 0 if "#" in condition else 1
        
        key = (condition, record)
        if key in self.cache:
            return self.cache[key]

        result = 0
        if condition[0] in ".?":
            result += self.recursive_count(condition[1:], record)
        
        if condition[0] in "#?":
            if record[0] <= len(condition) and not "." in condition[:record[0]] and (record[0] == len(condition) or condition[record[0]] != "#"):
                # The 1: is because we must end with a . 
                result += self.recursive_count(condition[record[0]+1:], record[1:])

        self.cache[key] = result        
        return result

    def find_configurations(self, repeat = 1):
        total_count = 0
        for r in self.records:
            self.cache = {}
            condition, record = r

            condition = "?".join([condition] * repeat) 
            record = tuple(map(int, record.split(",") * repeat))

            total_count += self.recursive_count(condition, record)
        
        print(f"Total count recursively found is {total_count}")

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
    hot_springs.find_configurations(5)