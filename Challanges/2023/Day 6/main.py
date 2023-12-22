import os, sys

input_text = "test_races_1.txt"

class Boat:
    def __init__(self, races, record) -> None:
        self.races = races.strip()
        self.record = record

    def define_races(self):
        races = []
        for race in self.races.split("\n"):
            races.append(race.strip().split())

        print(races)
        self.races = races[:]

    def number_of_record_beaters(self):
        for race in range(1, len(self.races[0])):
            print(self.races[0][race])
            
if __name__ == "__main__":
    path = os.path.dirname(__file__)
    file = os.path.join(path, input_text)

    if not os.path.exists(file):
        print(f"Invalid file supplied of {input_text}")
        sys.exit(1)

    with open(file, "r") as f:
        races = f.read()

    record = 9

    boat = Boat(races, record)
    boat.define_races()
    boat.number_of_record_beaters()