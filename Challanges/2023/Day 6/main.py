import os, sys

input_text = "puzzle_races_1.txt"

class Boat:
    def __init__(self, races) -> None:
        self.races = races.strip()

    def define_races(self):
        races = []
        for race in self.races.split("\n"):
            races.append(race.strip().split())
        self.races = races[:]

    def number_of_ways_to_beat_record(self, race_time, race_distance_record):
        can_beat_record = 0
        found_first = False
        for speed in range(0, race_time):
            distance_traveled = speed * (race_time-speed)
            if distance_traveled > race_distance_record:
                can_beat_record += 1
                found_first = True
            elif found_first:
                # If we've found a current first one we know everything
                # else won't beat the record so we can skip 
                break
        
        return can_beat_record

    def number_of_record_beaters(self):
        # Solution to task 1
        current_multiples = 1
        for race in range(1, len(self.races[0])):
            can_beat_record = self.number_of_ways_to_beat_record(int(self.races[0][race]), int(self.races[1][race]))

            if can_beat_record != 0:
                current_multiples *= can_beat_record

        return current_multiples
    
    def number_of_record_beaters_task_2(self):
        # Solution to task 2
        return self.number_of_ways_to_beat_record(int("".join(self.races[0][1:])), int("".join(self.races[1][1:])))
            
if __name__ == "__main__":
    path = os.path.dirname(__file__)
    file = os.path.join(path, input_text)

    if not os.path.exists(file):
        print(f"Invalid file supplied of {input_text}")
        sys.exit(1)

    with open(file, "r") as f:
        races = f.read()

    boat = Boat(races)
    boat.define_races()
    print(boat.number_of_record_beaters())
    print(boat.number_of_record_beaters_task_2())
