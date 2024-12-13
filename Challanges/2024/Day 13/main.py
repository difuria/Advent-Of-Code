from Inputs.puzzle_inputs import puzzle_input_1
from Inputs.test_inputs import test_input_1, test_input_2

import re


def build_puzzles(text: str, prize_adjustment: int = 0) -> list[dict[str, int]]:
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
                    "X": int(prize[0][0]) + prize_adjustment,
                    "Y": int(prize[0][1]) + prize_adjustment
                }

        puzzles.append(current)
    
    return puzzles


def calculate_fewest_tokens_brute_force(puzzle: dict[str, int]) -> int:
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


def calculate_fewest_tokens(puzzle: dict[str, int]) -> int:
    # s = (px*by - py*bx) / (ax*by - ay * bx)
    s = (
        (puzzle["prize"]["X"] * puzzle["B"]["Y"]) - (puzzle["prize"]["Y"] * puzzle["B"]["X"])
    ) / \
    (
        (puzzle["A"]["X"] * puzzle["B"]["Y"]) - (puzzle["A"]["Y"] * puzzle["B"]["X"])
    )

    # Not a whole number so it's not possible
    if s != int(s):
        return -1
    
    t = (
        puzzle["prize"]["X"] - (puzzle["A"]["X"] * s) # find the remaining sum
    ) / puzzle["B"]["X"]

    if t != int(t):
        return -1
    
    return int((s*3) + t)


def sum_puzzle_tokens(puzzles: list[dict[str, int]]):
    tokens = 0
    for puzzle in puzzles:
        fewest_tokens = calculate_fewest_tokens(puzzle)
        if fewest_tokens > -1:
            tokens += fewest_tokens
    
    print(f"The fewest tokens to win all the puzzles is {tokens}.")
    return tokens

print("Task 1")
puzzles = build_puzzles(test_input_1)
sum_puzzle_tokens(puzzles)

puzzles = build_puzzles(puzzle_input_1)
sum_puzzle_tokens(puzzles)

print("\nTask 2")
puzzles = build_puzzles(test_input_2)
sum_puzzle_tokens(puzzles)

puzzles = build_puzzles(puzzle_input_1, 10000000000000)
sum_puzzle_tokens(puzzles)

"""
So this is actual a single solution problem and there aren't multiple solutions.
So instead of brute force we can calculate what the multiples should be. 

S = times to multiple 1 button
T = times to multiple the other button
px = X prize location
bx = B X button press
etc

ax*s + bx*t = px -> times this by by
ay*s + by*t = py -> times this by bx

ax*s*by + bx*t*by = px*by
ay*s*bx + by*t*bx = py*bx

ax*s*by + bx*t*by - px*by = ay*s*bx + by*t*bx - py*bx
ax*s*by - px*by = ay*s*bx - py*bx
ax*s*by = ay*s*bx - py*bx + px*by
ax*s*by - ay*s*bx = px*by - py*bx
s(ax*by - ay * bx) = px*by - py*bx
s = (px*by - py*bx) / (ax*by - ay*bx)

Once we have s we can work out t with something as simple as:
t = (px - (ax*s)) / bx

Then if it's a whole number we know it's divisible.
Or we could check it's exactly equal.
"""