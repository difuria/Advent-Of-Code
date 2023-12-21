import os, sys

input_text = "puzzle_input_part_2.txt"

class Games:
    def __init__(self, games) -> None:
        self.games = games
        self.game_info = {}

    def analyse_games(self):
        pass

if __name__ == "__main__":
    path = os.path.dirname(__file__)
    file = os.path.join(path, input_text)

    if not os.path.exists(file):
        print(f"Invalid file supplied of {input_text}")
        sys.exit(1)

    with open(file, "r") as f:
        games = f.read()