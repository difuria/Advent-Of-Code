import os, sys

input_text = "puzzle_stacks_1.txt"

class  SupplyStacks:
    def __init__(self):
        self.__rest_stacks()

    def __rest_stacks(self):
        self.stacks = {}
        self.movements = []

    def load_stacks(self, stack_file):
        self.__rest_stacks()

        stacks, movements = stack_file.split("\n\n")
        for movement in movements.strip().split("\n"):
            self.movements.append(movement.split())

        stack_rows = stacks.split("\n")
        for stack_id in stack_rows[-1].split():
            self.stacks[stack_id] = []

        for stack in stack_rows[:-1]:
            index = 1
            for stack_id in self.stacks.keys():
                if stack[index] != " ":
                    self.stacks[stack_id].insert(0, stack[index])
                index += 4
    
    def move_stacks(self, move_at_a_time = 1):
        for movement in self.movements:
            number_to_move = int(movement[1])
            from_location = movement[3]
            to_location = movement[5]
     
            left_to_move = number_to_move
            while left_to_move > 0:
                if move_at_a_time == -1:
                    move_number = left_to_move
                elif left_to_move < move_at_a_time:
                    move_number = left_to_move
                else:
                    move_number = move_at_a_time

                self.stacks[to_location] += self.stacks[from_location][-move_number:]
                self.stacks[from_location] = self.stacks[from_location][:-move_number]
                left_to_move -= move_number

        top_blocks = ""
        for stacks in self.stacks.values():
            if len(stacks) > 0:
                top_blocks += stacks[-1]
        
        print(f"Top blocks {top_blocks}.")

def get_file(path, file):
    file = os.path.join(path, f"Inputs", file)

    if not os.path.exists(file):
        print(f"Invalid file supplied of {file}")
        sys.exit(1)

    with open(file, "r") as f:
        path_info = f.read()

    return path_info

if __name__ == "__main__":
    path = os.path.dirname(__file__)
    
    supply_stacks = SupplyStacks()
    supply_stacks.load_stacks(get_file(path, input_text))
    supply_stacks.move_stacks()
    supply_stacks.load_stacks(get_file(path, input_text))
    supply_stacks.move_stacks(-1)
