import math, os, re, sys

input_text = "puzzle_scratch_card_2.txt"

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
            for drawn_number in drawn_numbers.strip().split():
                if re.search(r"^(" + potential_winning_numbers + r")$", drawn_number):
                    winning_numbers.append(int(drawn_number))

            if winning_numbers:
                total += int(math.pow(2, len(winning_numbers)-1))
        
        return total

    def find_winning_cards(self):
        won_cards = {}
        for i, card in enumerate(self.scratch_cards):
            card_number, values = card.split(":")
            potential_winning_numbers, drawn_numbers = values.split("|")
            potential_winning_numbers = potential_winning_numbers.strip().replace(" ", "|")

            winning_numbers = []
            for drawn_number in drawn_numbers.strip().split():
                if re.search(r"^(" + potential_winning_numbers + r")$", drawn_number):
                    winning_numbers.append(int(drawn_number))

            if winning_numbers:
                for j in range(i+1, i+len(winning_numbers)+1):
                    current_card_id = i+1
                    won_card_id = j + 1
                    if won_card_id not in won_cards:
                        won_cards[won_card_id] = 0

                    won_cards[won_card_id] += 1

                    if i+1 in won_cards:
                        won_cards[won_card_id] += won_cards[current_card_id]

        total_scratch_cards = 0
        for i, card in enumerate(self.scratch_cards):
            current_card_id = i+1

            if current_card_id in won_cards:
                total_scratch_cards += won_cards[current_card_id]
            total_scratch_cards += 1
        
        return total_scratch_cards

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

    print(scratch_cards.find_winning_cards())