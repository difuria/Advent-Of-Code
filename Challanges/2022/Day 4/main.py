import os, sys

input_text = "puzzle_assignments_1.txt"

class CampCleanup:
    def __init__(self, assignments):
        self.assignments = assignments.strip().split("\n")
    
    def fully_contained_assignments(self):
        contained_assignments_count = 0
        for assignment in self.assignments:
            elf_1, elf_2 = assignment.split(",")
            elf_1_start, elf_1_end = list(map(int, elf_1.split("-")))
            elf_2_start, elf_2_end = list(map(int, elf_2.split("-")))

            if (elf_1_start <= elf_2_start and elf_1_end >= elf_2_end) or \
                (elf_2_start <= elf_1_start and elf_2_end >= elf_1_end):
                contained_assignments_count += 1
        
        print(f"Number of contained assignments {contained_assignments_count}.")
    
    def any_overlapping_assignments(self):
        overlapping_assignments = 0
        for assignment in self.assignments:
            elf_1, elf_2 = assignment.split(",")
            elf_1_start, elf_1_end = list(map(int, elf_1.split("-")))
            elf_2_start, elf_2_end = list(map(int, elf_2.split("-")))     

            if (elf_1_start >= elf_2_start and elf_2_end >= elf_1_start) or \
                (elf_2_start >= elf_1_start and elf_1_end >= elf_2_start) or \
                (elf_1_end >= elf_2_end and elf_1_start <= elf_2_end) or \
                (elf_2_end >= elf_1_end and elf_2_start <= elf_1_end):
                overlapping_assignments +=1 
        
        print(f"Number of overlapping assignments {overlapping_assignments}.")

if __name__ == "__main__":
    path = os.path.dirname(__file__)
    file = os.path.join(path, input_text)

    if not os.path.exists(file):
        print(f"Invalid file supplied of {input_text}")
        sys.exit(1)

    with open(file, "r") as f:
        assignments = f.read()

    camp_cleanup = CampCleanup(assignments)
    camp_cleanup.fully_contained_assignments()
    camp_cleanup.any_overlapping_assignments()
