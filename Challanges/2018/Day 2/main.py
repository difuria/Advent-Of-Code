import os, sys

def get_file(path, file):
    file = os.path.join(path, f"Task Inputs", file)

    if not os.path.exists(file):
        print(f"Invalid file supplied of {file}")
        sys.exit(1)

    with open(file, "r") as f:
        path_info = f.read()

    return path_info

def find_common_letters(boxes, differing_characters = 1):
    for i in range(len(boxes)-1):
        for j in range(1, len(boxes)):
            if len(boxes[i]) != len(boxes[j]):
                continue

            common_letters = ""
            for k in range(len(boxes[i])):
                if boxes[i][k] == boxes[j][k]:
                    common_letters += boxes[i][k]
            
            if len(boxes[i]) - differing_characters == len(common_letters):
                print(f"Common letters {common_letters}")
                return
    

if __name__ == "__main__":
    path = os.path.dirname(__file__)

    print("Task 1")
    boxes = get_file(path, "puzzle_box_1.txt").strip().split("\n")

    twos = 0
    threes = 0
    for input in boxes:
        counter = {}
        for letter in input:
            if not letter in counter:
                counter[letter] = 0
            counter[letter] += 1
    
        two_counted = False
        three_counted = False
        for item, value in counter.items():
            if value == 2 and not two_counted:
                twos += 1
                two_counted = True
            elif value == 3 and not three_counted:
                threes += 1
                three_counted = True

    print(f"Checksum is {twos * threes}")


    print("\nTask2")
    boxes = get_file(path, "puzzle_box_1.txt").strip().split("\n")
    find_common_letters(boxes)

