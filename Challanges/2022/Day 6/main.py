import os, sys

def get_file(path, file):
    file = os.path.join(path, f"Task Inputs", file)

    if not os.path.exists(file):
        print(f"Invalid file supplied of {file}")
        sys.exit(1)

    with open(file, "r") as f:
        path_info = f.read()

    return path_info

def find_marker(datasteam, length = 4):
    for i in range(0, len(datasteam)-length):
        number_of_unique_characters = len(set(list(datasteam[i:i+length])))

        if number_of_unique_characters == length:
            print(f"First marker, for length {length}, is character {i + length}")
            return

if __name__ == "__main__":
    path = os.path.dirname(__file__)

    for i in range(1, 6):
        find_marker(get_file(path, f"test_datastream_{i}.txt"))
        find_marker(get_file(path, f"test_datastream_{i}.txt"), 14)
    
    find_marker(get_file(path, f"puzzle_datastream_1.txt"))
    find_marker(get_file(path, f"puzzle_datastream_1.txt"), 14)