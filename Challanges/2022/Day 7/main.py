import os, sys
from copy import deepcopy

input_text = "puzzle_terminal_output_1.txt"

class SpaceLeft:
    def __init__(self, commands, file_system_size = 70000000):
        self.commands = commands.strip().split("\n")
        self.file_system_size = file_system_size

    def analyse_commands(self):
        info = { "directories": [], "files": [], "size": 0 }
        self.locations = { "/": deepcopy(info) }
        location = "/"
        for command in self.commands:
            command = command.strip()
            if command[0] == "$": # We have a command
                if command[2:4] == "cd":
                    l = command[5:]
                    
                    if l[0] == "/":
                        location = l
                    elif l == "..":
                        location = "/".join(location.split("/")[:-1])
                        if location == "":
                            location = "/"
                    elif l != ".":
                        if location != "/":
                            location += "/"
                        location += l

                    if not location in self.locations:
                        self.locations[location] = deepcopy(info)
            else:
                if command[0:3] == "dir":
                    subdir = location
                    if location != "/":
                        subdir += "/"
                    subdir += command[4:]
                    self.locations[location]["directories"].append(subdir)

                    if not subdir in self.locations:
                        self.locations[subdir] = deepcopy(info)
                else:
                    self.locations[location]["files"].append(command.split())

    def get_directory_size(self, directory = "/"):
        size = 0
        if not directory in self.locations:
            print(f"Unknown directory {directory}")
            return

        if self.locations[directory]["files"]:
            for f in self.locations[directory]["files"]:
                size += int(f[0])

        if self.locations[directory]["directories"]:
            for dir in self.locations[directory]["directories"]:
                size += self.get_directory_size(dir)

        self.locations[directory]["size"] = size

        return size
    
    def sum_directories_of_size(self, size = 100000):
        sum_size = 0
        for directory_values in self.locations.values():
            if directory_values["size"] <= size:
                sum_size += directory_values["size"]
        
        print(f"Sum of sizes was {sum_size}")

    def find_smallest_directory_to_delete(self, size = 30000000):
        smallest_size = float('inf')
        size = size - (self.file_system_size - self.locations["/"]["size"])
        for directory_values in self.locations.values():
            if directory_values["size"] >= size and directory_values["size"] < smallest_size:
                smallest_size = directory_values["size"]
        
        print(f"Delete directory of size {smallest_size}.")

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

    space_left = SpaceLeft(get_file(path, input_text))
    space_left.analyse_commands()

    space_left.get_directory_size()
    space_left.sum_directories_of_size()
    space_left.find_smallest_directory_to_delete()
