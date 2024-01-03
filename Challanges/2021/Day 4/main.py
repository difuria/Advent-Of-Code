import os, sys

input_text = "puzzle_game_1.txt"

class GiantSquid():
    def __init__(self):
        self.drawn_numbers = []
        self.boards = []
        self.marked_boards = []
        # Value -> Board -> X, Y Locations
        self.value_locations = {}
        # Board -> x, y ticked off
        self.game_cards = {}

        self.boards = []
        self.board_width = 0
        self.board_height = 0

    def load_games(self, game_input):
        self.value_locations = {}
        self.game_cards = {}

        split_input = game_input.strip().split("\n\n")
        self.drawn_numbers = split_input[0].split(",")

        self.boards = []
        for game_id, board in enumerate(split_input[1:]):
            self.game_cards[game_id] = { "x":{}, "y":{} }

            self.boards.append([])
            board = board.split("\n")
            self.board_height = len(board)

            for y, line in enumerate(board):
                self.game_cards[game_id]["y"][y] = []
                line = line.split()
                self.boards[-1].append(line)
                self.board_width = len(line)
                for x, item in enumerate(line):
                    self.game_cards[game_id]["x"][x] = []
                    if not item in self.value_locations:
                        self.value_locations[item] = {}
                    if not game_id in self.value_locations[item]:
                        self.value_locations[item][game_id] = {}
                    
                    self.value_locations[item][game_id] = {
                        "x": x,
                        "y": y
                    }

    def __find_unticked(self, board, index):
        unticked_multiple = 0
        for y in self.boards[board]:
            for x in y:
                if not x in self.drawn_numbers[:index+1]:
                    unticked_multiple += int(x)
        
        return unticked_multiple

    
    def play_game(self):
        for index, drawn_number in enumerate(self.drawn_numbers):
            if drawn_number in self.value_locations:
                for board, position in self.value_locations[drawn_number].items():
                    x = position["x"]
                    y = position["y"]
                    self.game_cards[board]["x"][x].append(drawn_number)
                    self.game_cards[board]["y"][y].append(drawn_number)

                    if len(self.game_cards[board]["x"][x]) == self.board_width or len(self.game_cards[board]["y"][y]) == self.board_height:
                        print("Completed row")
                        print(f"Final Score {self.__find_unticked(board, index) * int(drawn_number)}")
                        return

def get_file(path, file):
    file = os.path.join(path, f"Task Inputs", file)

    if not os.path.exists(file):
        print(f"Invalid file supplied of {file}")
        sys.exit(1)

    with open(file, "r") as f:
        path_info = f.read()

    return path_info

if __name__ == "__main__":
    path = os.path.dirname(__file__)

    giant_quid = GiantSquid()
    giant_quid.load_games(get_file(path, input_text))
    giant_quid.play_game()
