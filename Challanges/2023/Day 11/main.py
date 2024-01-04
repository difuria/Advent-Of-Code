import os, sys

input_text = "puzzle_image_1.txt"

class CosmicExpansion:
    def __init__(self, image):
        self.original_image = image
        self.galaxy_locations = []

        self.empty_x = set()
        self.empty_y = set()

        self.load_image()

    def load_image(self, image = None):
        if image == None:
            split_image = self.original_image.strip().split("\n")
        else:
            self.original_image = image
            split_image = image.strip().split("\n")

        self.image = [list(row) for row in split_image]

    def check_image(self):
        self.galaxy_locations = []
        self.empty_x = set()
        for i, row in enumerate(self.image):
            if not "#" in row:
                self.empty_y.add(i)

        for i in range(len(self.image[0])):
            self.empty_x.add(i)
            for j in range(len(self.image)):
                if self.image[j][i] == "#":
                    self.empty_x.remove(i)
                    break

        # Last get the galaxy locations
        galaxy = 0
        for y in range(len(self.image)):
            for x in range(len(self.image[y])):
                if self.image[y][x] == "#":
                    self.galaxy_locations.append([x,y])
                    galaxy += 1

    def gather_shortest_locations(self, gap_distance = 2):
        distance = 0
        for i in range(len(self.galaxy_locations)-1):
            for j in range(i+1, len(self.galaxy_locations)):
                x_f_galaxy, y_f_galaxy = self.galaxy_locations[i]
                x_s_galaxy, y_s_galaxy = self.galaxy_locations[j]

                x_max = max(x_f_galaxy, x_s_galaxy)
                x_min = min(x_f_galaxy, x_s_galaxy)
                y_max = max(y_f_galaxy, y_s_galaxy)
                y_min = min(y_f_galaxy, y_s_galaxy)

                extra_rows_and_columns = 0
                for x in range(x_min, x_max):
                    if x in self.empty_x:
                        extra_rows_and_columns += gap_distance - 1

                for y in range(y_min, y_max):
                    if y in self.empty_y:
                        extra_rows_and_columns += gap_distance - 1       

                distance += (x_max - x_min) + (y_max - y_min) + extra_rows_and_columns
        
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

    cosmic_expansion.check_image()
    cosmic_expansion.gather_shortest_locations(1000000)
