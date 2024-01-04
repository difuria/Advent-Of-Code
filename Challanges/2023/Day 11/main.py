import os, sys

input_text = "puzzle_image_1.txt"

class CosmicExpansion:
    def __init__(self, image):
        self.original_image = image
        self.galaxy_locations = []

        self.load_image()

    def load_image(self, image = None):
        if image == None:
            split_image = self.original_image.strip().split("\n")
        else:
            self.original_image = image
            split_image = image.strip().split("\n")

        self.image = [list(row) for row in split_image]
        self.adjusted_image = [list(row) for row in split_image]

    def check_image(self):
        self.galaxy_locations = []
        no_galaxies_in_rows = []
        for i, row in enumerate(self.image):
            if "#" not in row:
                no_galaxies_in_rows.append(i)

        no_galaxies_in_cols = []
        for i, col in enumerate(self.image[0]):
            no_galaxies_in_cols.append(i)
            for j in range(len(self.image)):
                if self.image[j][i] == "#":
                    no_galaxies_in_cols.pop()
                    break

        for i, row in enumerate(no_galaxies_in_rows):
            self.adjusted_image.insert(row + i, ["."] * len(self.image[0]))
        
        for i, col in enumerate(no_galaxies_in_cols):
            for j in range(len(self.adjusted_image)):
                self.adjusted_image[j].insert(col + i, ".")

        # Last get the galaxy locations
        galaxy = 0
        for y in range(len(self.adjusted_image)):
            for x in range(len(self.adjusted_image[y])):
                if self.adjusted_image[y][x] == "#":
                    self.galaxy_locations.append([x,y])
                    galaxy += 1

    def gather_shortest_locations(self):
        distance = 0
        for i in range(len(self.galaxy_locations)-1):
            for j in range(i+1, len(self.galaxy_locations)):
                x_f_galaxy, y_f_galaxy = self.galaxy_locations[i]
                x_s_galaxy, y_s_galaxy = self.galaxy_locations[j]
                distance += abs(x_f_galaxy - x_s_galaxy) + abs(y_f_galaxy - y_s_galaxy)
        
        print(f"Distance {distance}")

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

    cosmic_expansion = CosmicExpansion(get_file(path, input_text))
    cosmic_expansion.check_image()
    cosmic_expansion.gather_shortest_locations()
