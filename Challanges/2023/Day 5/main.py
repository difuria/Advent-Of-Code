import os, sys

input_text = "puzzle_seed_mapping_1.txt"

class SeedMapping:
    def __init__(self, seed_mappings) -> None:
        self.seed_mappings = seed_mappings.strip()
        self.mappings = {}
        self.seeds = []

    def create_mappings(self):
        self.mappings = {}
        self.seeds = []

        for item in self.seed_mappings.split("\n\n"):
            key, mappings = item.split(":")
            
            if key == "seeds":
                self.seeds = list(map(int, mappings.strip().split()))
                continue
            elif not key in self.mappings:
                self.mappings[key] = []

            for mapping in mappings.strip().split("\n"):
                mapping_values = list(map(int, mapping.split()))

                self.mappings[key].append({
                    "new_position": mapping_values[0],
                    "current_position": mapping_values[1],
                    "range": mapping_values[2]
                })

    def map_item(self, key, item):
        for mapping in self.mappings[key]:
            if item >= mapping["current_position"] and item <= mapping["current_position"] + mapping["range"]:
                return (item - mapping["current_position"]) + mapping["new_position"]
        
        return item

    def locate_seeds(self, output = False):
        lowest_location = float('inf')
        for seed in self.seeds:
            soil = self.map_item("seed-to-soil map", seed)
            fertilizer = self.map_item("soil-to-fertilizer map", soil)
            water = self.map_item("fertilizer-to-water map", fertilizer)
            light = self.map_item("water-to-light map", water)
            temperature = self.map_item("light-to-temperature map", light)
            humidity = self.map_item("temperature-to-humidity map", temperature)
            location = self.map_item("humidity-to-location map", humidity)
            
            if output:
                print(f"Seed {seed}, soil {soil}, fertilizer {fertilizer}, water {water}, light {light}, temperature {temperature}, humidity {humidity}, location {location}.")

            lowest_location = min(lowest_location, location)
        
        return int(lowest_location)
    
    def locate_seed_range(self, output = False):
        # TODO this works but takes a couple of hours to run
        lowest_location = float('inf')
        for i in range(0, len(self.seeds), 2):
            for seed in range(self.seeds[i], self.seeds[i] + self.seeds[i+1]):
                soil = self.map_item("seed-to-soil map", seed)
                fertilizer = self.map_item("soil-to-fertilizer map", soil)
                water = self.map_item("fertilizer-to-water map", fertilizer)
                light = self.map_item("water-to-light map", water)
                temperature = self.map_item("light-to-temperature map", light)
                humidity = self.map_item("temperature-to-humidity map", temperature)
                location = self.map_item("humidity-to-location map", humidity)

                if output:
                    print(f"Seed {seed}, soil {soil}, fertilizer {fertilizer}, water {water}, light {light}, temperature {temperature}, humidity {humidity}, location {location}.")          

                lowest_location = min(lowest_location, location)
        
        return int(lowest_location)

if __name__ == "__main__":
    path = os.path.dirname(__file__)
    file = os.path.join(path, input_text)

    if not os.path.exists(file):
        print(f"Invalid file supplied of {input_text}")
        sys.exit(1)

    with open(file, "r") as f:
        seed_mappings = f.read()

    mappings = SeedMapping(seed_mappings)        
    mappings.create_mappings()
    print(f"Lowest Location for task 1 was: {mappings.locate_seeds()}")
    print(f"Lowest Location for task 2 was: {mappings.locate_seed_range()}")