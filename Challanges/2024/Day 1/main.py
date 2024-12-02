import os
import sys

def get_file(path: str, file: str) -> str:
    file = os.path.join(path, f"Task Inputs", file)

    if not os.path.exists(file):
        print(f"Invalid file supplied of {file}")
        sys.exit(1)

    with open(file, "r") as f:
        path_info = f.read()

    return path_info

if __name__ == "__main__":
    path = os.path.dirname(__file__)

    input_locations = get_file(path, "puzzle_input_1.txt").strip()

    location_lists = [[],[]]
    for pairing in input_locations.split("\n"):
        i, j = list(map(int, pairing.strip().split("   ")))
        location_lists[0].append(i)
        location_lists[1].append(j)
    
    for index in range(2):
        location_lists[index] = sorted(location_lists[index])

    distance = 0
    similarity_score = 0
    similarity_mapping = {}
    for index in range(len(location_lists[0])):
        distance += abs(location_lists[0][index] - location_lists[1][index])

        if location_lists[0][index] in similarity_mapping:
            similarity_score += similarity_mapping[location_lists[0][index]]
        else:
            score = (location_lists[1].count(location_lists[0][index]) * location_lists[0][index])
            similarity_score += score
            similarity_mapping[location_lists[0][index]] = score

    print(f"Total distance is: {distance}")
    print(f"Similarity score is: {similarity_score}")
