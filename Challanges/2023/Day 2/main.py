import os, re, sys

input_text = "puzzle_input_2.txt"

class Games:
    def __init__(self, games) -> None:
        self.games = games.strip().split("\n")
        self.valid_games = []

    def analyse_games(self, query):
        # Task 1 Solution
        self.valid_games = []

        for game in self.games:
            id, contents = game.split(":")

            valid = True
            for colour in query:
                colour_max = 0
                colour_balls = re.findall(r"(\d{1,}) " + colour, contents)
                for colour_ball in colour_balls:
                    colour_max = max(colour_max, int(colour_ball))

                    if query[colour] < colour_max:
                        valid = False
                        break

                if not valid:
                    break
            
            if valid:
                game_id = id.replace("Game ", "")
                self.valid_games.append(int(game_id))
    
    def sum_valid_games(self):
        return sum(self.valid_games)

    def find_minimum_number(self, query):
        # Task 2 Solution
        set_sum = 0
        for game in self.games:
            minimums = 1
            for colour in query:
                colour_max = 0
                colour_balls = re.findall(r"(\d{1,}) " + colour, game)
                for colour_ball in colour_balls:
                    colour_max = max(colour_max, int(colour_ball))

                minimums *= colour_max
            set_sum += minimums  

        return set_sum          

if __name__ == "__main__":
    path = os.path.dirname(__file__)
    file = os.path.join(path, input_text)

    if not os.path.exists(file):
        print(f"Invalid file supplied of {input_text}")
        sys.exit(1)

    with open(file, "r") as f:
        games_info = f.read()

    query = {
        "red": 12,
        "green": 13,
        "blue": 14
    }

    games = Games(games_info)
    games.analyse_games(query)
    print(games.sum_valid_games())

    print(games.find_minimum_number(query))