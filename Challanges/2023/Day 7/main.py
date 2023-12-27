import os, sys

input_text = "puzzle_hands_1.txt"

class CamelCards:
    def __init__(self, hands):
        self.hands = {}
        self.hands_input = hands

        # Used for comparison
        self.card_value = {}

        self.hand_value = {
            "5 of a Kind": 6,
            "4 of a Kind": 5,
            "Full House": 4,
            "3 of a Kind": 3,
            "2 Pair": 2,
            "Pair": 1,
            "High Card": 0
        }

    def __reset_hands(self):
        for hand in self.hands_input.strip().split("\n"):
            h, b = hand.split()
            self.hands[h] = { "Bid": int(b), "Cards": {}, "Type":"" }

    def __populate_values(self):
        for value, card in enumerate(self.cards):
            self.card_value[card] = value

    def __task_1_values(self):
        self.cards = "23456789TJQKA"
        self.__populate_values()

    def __task_2_values(self):
        self.cards = "J23456789TQKA"
        self.__populate_values()

    def evaluate_hands(self, task = 1):
        self.__reset_hands()
        for hand in self.hands:
            jokers = 0
            highest_card = ""
            for card in hand:
                if task == 2 and card == "J":
                    jokers += 1
                    continue

                if not card in self.hands[hand]["Cards"]:
                    self.hands[hand]["Cards"][card] = 0
                self.hands[hand]["Cards"][card] += 1

                if highest_card == "":
                    highest_card = card
                elif self.hands[hand]["Cards"][card] > self.hands[hand]["Cards"][highest_card]:
                    highest_card = card

            if task == 2:
                if highest_card == "":
                    self.hands[hand]["Cards"]["A"] = jokers
                else:
                    self.hands[hand]["Cards"][highest_card] += jokers

            if len(self.hands[hand]["Cards"].keys()) == 1:
                self.hands[hand]["Cards"]["Type"] = "5 of a Kind"
            elif len(self.hands[hand]["Cards"].keys()) == 2:
                card = list(self.hands[hand]["Cards"].keys())[0]
                if self.hands[hand]["Cards"][card] == 1 or self.hands[hand]["Cards"][card] == 4:
                    self.hands[hand]["Cards"]["Type"] = "4 of a Kind"
                else:
                    self.hands[hand]["Cards"]["Type"] = "Full House"
            elif len(self.hands[hand]["Cards"].keys()) == 3:
                for card in self.hands[hand]["Cards"]:
                    if self.hands[hand]["Cards"][card] == 2:
                        self.hands[hand]["Cards"]["Type"] = "2 Pair"
                        break
                    elif self.hands[hand]["Cards"][card] == 3:
                        self.hands[hand]["Cards"]["Type"] = "3 of a Kind"
                        break
            elif len(self.hands[hand]["Cards"].keys()) == 4:
                self.hands[hand]["Cards"]["Type"] = "Pair"
            else:
                self.hands[hand]["Cards"]["Type"] = "High Card"

    def first_hand_greater_than_second(self, hand_1, hand_2):
        h1_type = self.hands[hand_1]["Cards"]["Type"]
        h2_type = self.hands[hand_2]["Cards"]["Type"]

        if self.hand_value[h1_type] > self.hand_value[h2_type]:
            return True
        elif self.hand_value[h1_type] == self.hand_value[h2_type]:
            for card_index in range(len(hand_1)):
                h1_card = hand_1[card_index]
                h2_card = hand_2[card_index]
                if self.card_value[h1_card] > self.card_value[h2_card]:
                    return True
                elif self.card_value[h1_card] < self.card_value[h2_card]:
                    return False
        
        return False

    def total_winnings(self, task = 1):
        if task == 1:
            self.__task_1_values()
        else:
            self.__task_2_values()

        rankings = []
        for hand_info in self.hands:
            hand = hand_info

            if len(rankings) == 0:
                rankings.append(hand)
                continue

            added = False
            for index, current_rank in enumerate(rankings):
                if not self.first_hand_greater_than_second(hand, current_rank):
                    rankings = rankings[:index] + [hand] + rankings[index:]
                    added = True
                    break
            if not added:
                rankings.append(hand)

        winnings = 0
        for rank_index, hand in enumerate(rankings):
            winnings += (rank_index + 1) * self.hands[hand]["Bid"]
        
        print(f"Total winnings for task {task} was {winnings}.")

if __name__ == "__main__":
    path = os.path.dirname(__file__)
    file = os.path.join(path, input_text)

    if not os.path.exists(file):
        print(f"Invalid file supplied of {input_text}")
        sys.exit(1)

    with open(file, "r") as f:
        hands = f.read()

    camel_cards = CamelCards(hands)
    camel_cards.evaluate_hands()
    camel_cards.total_winnings()

    camel_cards.evaluate_hands(2)
    camel_cards.total_winnings(2)
