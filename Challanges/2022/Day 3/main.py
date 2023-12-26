import os, string, sys

input_text = "puzzle_bag_1.txt"

class RucksackReorganization:
    def __init__(self, bags):
        self.bags = bags.strip().split("\n")
        self.alphabet = string.ascii_lowercase + string.ascii_uppercase

    def sum_priorities(self):
        priorities = []
        for bag in self.bags:
            left_compartment = bag[:len(bag)//2]
            right_compartment = bag[len(bag)//2:]
            for letter in left_compartment:
                if letter in right_compartment:
                    priorities.append(self.alphabet.index(letter)+1)
                    break
        
        print(f"Sum of priorities is {sum(priorities)}")
    
    def common_elf_group_item(self, group_size = 3):
        priorities = []
        for bag_index in range(0, len(self.bags), group_size):
            for letter in self.bags[bag_index]:
                if letter in self.bags[bag_index+1] and letter in self.bags[bag_index+2]:
                    priorities.append(self.alphabet.index(letter)+1)
                    break                
        
        print(f"Sum of priorities is {sum(priorities)}")

if __name__ == "__main__":
    path = os.path.dirname(__file__)
    file = os.path.join(path, input_text)

    if not os.path.exists(file):
        print(f"Invalid file supplied of {input_text}")
        sys.exit(1)

    with open(file, "r") as f:
        bags = f.read()

    rucksack_reorganization = RucksackReorganization(bags)
    rucksack_reorganization.sum_priorities()
    rucksack_reorganization.common_elf_group_item()
