import math, os, re, sys

input_text = "puzzle_scatch_card_1.txt"

class ScratchCards:
    def __init__(self, scratch_cards) -> None:
        self.scratch_cards = scratch_cards.strip().split("\n")

    def find_winnings(self):
        # Solution to task 1
        total = 0
        for card in self.scratch_cards:
            card_number, values = card.split(":")
            potential_winning_numbers, drawn_numbers = values.split("|")
            potential_winning_numbers = potential_winning_numbers.strip().replace(" ", "|")

            winning_numbers = []
            for drawn_number in drawn_numbers.strip().split(" "):
                if drawn_number.strip() == "":
                    continue
                elif re.search(r"^(" + potential_winning_numbers + r")$", drawn_number):
                    winning_numbers.append(int(drawn_number))

            if winning_numbers:
                total += int(math.pow(2, len(winning_numbers)-1))
        
        return total

    def find_winning_cards(self):
        pass

if __name__ == "__main__":
    path = os.path.dirname(__file__)
    file = os.path.join(path, input_text)

    if not os.path.exists(file):
        print(f"Invalid file supplied of {input_text}")
        sys.exit(1)

    with open(file, "r") as f:
        list_of_scatch_cards = f.read()
    
    scratch_cards = ScratchCards(list_of_scatch_cards)
    print(scratch_cards.find_winnings())