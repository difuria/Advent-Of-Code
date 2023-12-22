import os, sys

input_text = "puzzle_strategy.txt"

class RockPaperScissors:
    def __init__(self, rounds) -> None:
        self.rounds = rounds.strip().split("\n")

        self.options = {
            "A": "Rock",
            "B": "Paper",
            "C": "Scissors"
        }
        self.options["X"] = self.options["A"]
        self.options["Y"] = self.options["B"]
        self.options["Z"] = self.options["C"]

        self.value = {
            "Rock": 1,
            "Paper": 2,
            "Scissors": 3
        }

        self.actions = {
            "X": "Lose",
            "Y": "Draw",
            "Z": "Win"
        }

    def rock_paper_scissors(self, player_1_plays, player_2_plays):
        if player_1_plays == player_2_plays:
            return "Draw"
        elif player_1_plays == "Rock" and player_2_plays == "Scissors":
            return "Player 1"
        elif player_1_plays == "Scissors" and player_2_plays == "Paper":
            return "Player 1"
        elif player_1_plays == "Paper" and player_2_plays == "Rock":
            return "Player 1"
        else:
            return "Player 2"
    
    def calculate_score(self):
        # Solution to task 1
        total_score = 0
        for round in self.rounds:
            player_1, player_2 = round.split()

            outcome = self.rock_paper_scissors(self.options[player_1], self.options[player_2])

            if outcome == "Draw":
                total_score += 3
            elif outcome == "Player 2":
                total_score += 6
            
            total_score += self.value[self.options[player_2]]
        
        return total_score
    
    def action_taken(self, action, player_1_plays):
        if action == "Draw":
            return player_1_plays
        elif action == "Lose":
            if player_1_plays == "Rock":
                return "Scissors"
            elif player_1_plays == "Paper":
                return "Rock"
            else:
                return "Paper"
        elif action == "Win":
            if player_1_plays == "Rock":
                return "Paper"
            elif player_1_plays == "Paper":
                return "Scissors"
            else:
                return "Rock"

    def calculate_from_guide(self):
        # Solution to task 2
        total_score = 0
        for round in self.rounds:
            player_1, player_2 = round.split()

            action_taken = self.action_taken(self.actions[player_2], self.options[player_1])

            total_score += self.value[action_taken]
            if self.actions[player_2] == "Draw":
                total_score += 3
            elif self.actions[player_2] == "Win":
                total_score += 6           
        
        return total_score

if __name__ == "__main__":
    path = os.path.dirname(__file__)
    file = os.path.join(path, input_text)

    if not os.path.exists(file):
        print(f"Invalid file supplied of {input_text}")
        sys.exit(1)

    with open(file, "r") as f:
        rounds = f.read()

    rock_paper_scissors = RockPaperScissors(rounds)
    print(f"What to play score: {rock_paper_scissors.calculate_score()}")
    print(f"Action to play score: {rock_paper_scissors.calculate_from_guide()}")