import os, sys

input_text = "puzzle_schema_1.txt"

class GearRatios:
    def __init__(self, engine_schematic) -> None:
        self.engine_schematic = engine_schematic.strip().split("\n")

        self.valid_numbers = []
        self.invalid_numbers = []
    
    def search_schematic(self):
        current_integer = {}
        for line_index, line in enumerate(self.engine_schematic):
            for character_index, character in enumerate(line):
                if character.isdigit():
                    current_integer["y"] = line_index
                    
                    if "x" not in current_integer:
                        current_integer["x"] = { "start":character_index }
                        current_integer["value"] = character
                    else:
                        current_integer["value"] += character
                    
                    current_integer["x"]["end"] = character_index

                else:
                    if current_integer:
                        self.search_valid_integer(current_integer)
                        current_integer = {}
            
            if current_integer:
                self.search_valid_integer(current_integer)

            # They don't appear to cross lines so we can reset at any point
            current_integer = {}
    
    def search_valid_integer(self, current_integer):
        y_start = current_integer["y"]
        if current_integer["y"] > 0:
            y_start -= 1
        
        y_end = current_integer["y"] + 1
        if current_integer["y"] < len(self.engine_schematic) - 1:
            y_end += 1

        for y in range(y_start, y_end):

            x_start = current_integer["x"]["start"]
            if current_integer["x"]["start"] > 0:
                x_start -= 1
            
            x_end = current_integer["x"]["end"] + 1
            if current_integer["x"]["end"] < len(self.engine_schematic[y]) - 1:
                x_end += 1

            for x in range(x_start, x_end):
                if y == current_integer["y"] and (x <= current_integer["x"]["end"] and x >= current_integer["x"]["start"]):
                    continue

                if not self.engine_schematic[y][x].isdigit() and not self.engine_schematic[y][x].isalpha() and self.engine_schematic[y][x] != ".":
                    self.valid_numbers.append(int(current_integer["value"]))
                    return
        
        self.invalid_numbers.append(int(current_integer["value"]))
    
    def sum_valid(self):
        return sum(self.valid_numbers)
        

if __name__ == "__main__":
    path = os.path.dirname(__file__)
    file = os.path.join(path, input_text)

    if not os.path.exists(file):
        print(f"Invalid file supplied of {input_text}")
        sys.exit(1)

    with open(file, "r") as f:
        engine_schematic = f.read()

    gear_ratios = GearRatios(engine_schematic)
    gear_ratios.search_schematic()
    print(gear_ratios.sum_valid())