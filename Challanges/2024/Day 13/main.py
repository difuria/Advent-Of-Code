from Inputs.puzzle_inputs import puzzle_input_1
from Inputs.test_inputs import test_input_1, test_input_2

import re

def build_puzzles(text: str) -> list[dict[str, int]]:
    split_puzzles = text.strip().split("\n\n")

    puzzles = []
    for puzzle in split_puzzles:
        current = {}
        for line in puzzle.split("\n"):
            buttons = re.findall(r"Button (A|B):\s{1,}X\+(\d{1,}),\s{1,}Y\+(\d{1,})", line)
            prize = re.findall(r"Prize:\s{1,}X=(\d{1,}),\s{1,}Y=(\d{1,})", line)
            if buttons:
                current[buttons[0][0]] = {
                    "X": int(buttons[0][1]),
                    "Y": int(buttons[0][2])
                }
            
            if prize: 
                current["prize"] = {
                    "X": int(prize[0][0]),
                    "Y": int(prize[0][1])
                }

        puzzles.append(current)
    
    return puzzles


def calculate_fewest_tokens(puzzle: dict[str, int]) -> int:
    multiple_a = 0
    while True:
        x_remaining = puzzle["prize"]["X"] - (multiple_a * puzzle["A"]["X"])
        y_remaining = puzzle["prize"]["Y"] - (multiple_a * puzzle["A"]["Y"])

        multiple_b = x_remaining // puzzle["B"]["X"]

        if ((multiple_a * puzzle["A"]["X"]) + (multiple_b * puzzle["B"]["X"])) == puzzle["prize"]["X"] and \
            ((multiple_a * puzzle["A"]["Y"]) + (multiple_b * puzzle["B"]["Y"])) == puzzle["prize"]["Y"]:
            return (multiple_a * 3) + multiple_b
        elif x_remaining <= -1 or y_remaining <= -1:
            return -1
        
        multiple_a += 1


def sum_puzzle_tokens(puzzles: list[dict[str, int]]):
    tokens = 0
    for puzzle in puzzles:
        fewest_tokens = calculate_fewest_tokens(puzzle)
        if fewest_tokens > -1:
            tokens += fewest_tokens
    
    print(f"The fewest tokens to win all the puzzles is {tokens}.")
    return tokens

puzzles = build_puzzles(test_input_1)
sum_puzzle_tokens(puzzles)

puzzles = build_puzzles(puzzle_input_1)
sum_puzzle_tokens(puzzles)
