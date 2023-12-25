import os, sys

input_text = "puzzle_dive_1.txt"

class Dive:
    def __init__(self, dive_report):
        self.dive_report = dive_report.strip().split("\n")
        self.reset_location()

    def reset_location(self):
        self.location = {
            "aim": 0,
            "depth": 0,
            "position": 0
        }

    def find_location(self):
        # Solution to task 1
        self.reset_location() 
        for action in self.dive_report:
            direction, movement = action.split()
            if direction == "forward":
                self.location["position"] += int(movement)
            elif direction == "up":
                self.location["depth"] -= int(movement)
            elif direction == "down":
                self.location["depth"] += int(movement)
        
        print(self.location["depth"] * self.location["position"])

    def find_aim(self):
        # Solution to task 2
        self.reset_location() 
        for action in self.dive_report:
            direction, movement = action.split()
            if direction == "forward":
                self.location["position"] += int(movement)
                self.location["depth"] += self.location["aim"] * int(movement)
            elif direction == "up":
                self.location["aim"] -= int(movement)
            elif direction == "down":
                self.location["aim"] += int(movement)
        
        print(self.location["depth"] * self.location["position"])

if __name__ == "__main__":
    path = os.path.dirname(__file__)
    file = os.path.join(path, input_text)

    if not os.path.exists(file):
        print(f"Invalid file supplied of {input_text}")
        sys.exit(1)

    with open(file, "r") as f:
        dive_report = f.read()

    dive = Dive(dive_report)
    dive.find_location()
    dive.find_aim()
