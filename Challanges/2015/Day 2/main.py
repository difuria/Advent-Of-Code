import os
import sys

def get_file(path:str, file:str) -> str:
    file = os.path.join(path, f"Task Inputs", file)

    if not os.path.exists(file):
        print(f"Invalid file supplied of {file}")
        sys.exit(1)

    with open(file, "r") as f:
        path_info = f.read()

    return path_info

if __name__ == "__main__":
    path = os.path.dirname(__file__)

    presents = get_file(path, "puzzle_input_1.txt")

    total_wrapping_paper = 0
    total_ribben = 0
    for present in presents.split("\n"):
        present = sorted(list(map(int, present.split("x"))))

        sides_areas = sorted([
            present[0] * present[1],
            present[1] * present[2],
            present[2] * present[0]
        ])
        
        wrapping_required = 0
        ribben_required = 0
        for side in sides_areas:
            wrapping_required += (2*side)

        side_length = sorted([
            (2 * present[0]) + (2 * present[1]),
            (2 * present[1]) + (2 * present[2]),
            (2 * present[2]) + (2 * present[0])          
        ])
        ribben_required += (
            (2 * present[0]) + (2 * present[1]) +
            (present[0] * present[1] * present[2])
        )
        print(f"Ribben {ribben_required}")

        wrapping_required += sides_areas[0]
        total_wrapping_paper += wrapping_required

        total_ribben += ribben_required

    print(f"Total Required Wrapping Paper: {total_wrapping_paper}")
    print(f"Total Required Ribben : {total_ribben}")