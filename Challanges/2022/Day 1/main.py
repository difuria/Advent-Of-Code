import os, sys

input_text = "puzzle_elf_calories_1.txt"

class Carlories:
    def __init__(self, elf_carry) -> None:
        self.elf_carry = elf_carry

    def calorie_carrying(self):
        carrying_totals = []
        for elf in self.elf_carry.split("\n\n"):
            carrying = list(map(int, elf.split("\n")))
            carrying_totals.append(sum(carrying))
        
        carrying_totals.sort()
        return carrying_totals
    
    def top_calorie_carrying(self):        
        return self.calorie_carrying()[-1]
    
    def top_3_calorie_carrying(self):
        return sum(self.calorie_carrying()[-3:])

if __name__ == "__main__":
    path = os.path.dirname(__file__)
    file = os.path.join(path, input_text)

    if not os.path.exists(file):
        print(f"Invalid file supplied of {input_text}")
        sys.exit(1)

    with open(file, "r") as f:
        elf_carry = f.read()

    calories = Carlories(elf_carry)
    print(f"Top Carry: {calories.top_calorie_carrying()}")
    print(f"Top 3 Carry: {calories.top_3_calorie_carrying()}")