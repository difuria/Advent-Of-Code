from Inputs.puzzle_inputs import puzzle_input_1
from Inputs.test_inputs import test_input


def blink_stones(text: str, blinks: int) -> list[int]:
    stones = list(map(int, text.strip().split()))

    index = 0
    for blink in range(blinks):
        index = 0
        while index < len(stones):
            if stones[index] == 0:
                stones[index] = 1
                index += 1
            elif len(str(stones[index])) % 2 == 0:
                str_stone = str(stones[index])
                stone_length = len(str_stone)
                new_stones = str_stone[:stone_length//2], str_stone[stone_length//2:]

                stones.insert(index, int(new_stones[0]))
                index += 1
                stones.insert(index, int(new_stones[1]))
                index += 1
                stones.pop(index)
            else:
                stones[index] *= 2024
                index += 1

    return stones


def blink_stones_2(text: str, blinks: int) -> list[int]:
    stones = list(map(int, text.strip().split()))

    # Stone value, Number of blinks against it
    stones = []
    for stone in text.strip().split():
        stones.append([int(stone), 0])

    # For each stone store the value created at the number of blinks 
    memory = {}

    index = 0
    while index < len(stones):
        for i in range(stones[index][1], blinks):
            current_index = index
            if stones[current_index][0] == 0:
                stones[current_index][0] = 1
                current_index += 1
            elif len(str(stones[current_index][0])) % 2 == 0:
                str_stone = str(stones[current_index][0])
                stone_length = len(str_stone)
                new_stones = str_stone[:stone_length//2], str_stone[stone_length//2:]
                stones.insert(current_index, [int(new_stones[0]), i+1])
                current_index += 1
                stones.insert(current_index, [int(new_stones[1]), i+1])
                current_index += 1
                stones.pop(current_index)
            else:
                stones[current_index][0] *= 2024
                current_index += 1
            
            stones[index][1] += 1
        
        index += 1
    
    return stones


print("Test Inputs")
test_count = 0
passed = 0
for test in ["1", "2"]:
    test_count += 1
    print(f"Test {test}.")
    stones = blink_stones(test_input[test]["Input"]["stones"], test_input[test]["Input"]["blinks"])

    if stones == list(map(int, test_input[test]["Answers"]["Task 1"]["output"].split())):
        passed += 1
        print(f"passed")
    else:
        print(f"failed")

stones = blink_stones_2(puzzle_input_1, 25)

if passed == test_count:
    print("\nAll test cases passed, running puzzle input.")
    stones = blink_stones(puzzle_input_1, 25)
    print(f"There will be a total of {len(stones)} after 25 blinks.")
    stones = blink_stones_2(puzzle_input_1, 75) # This attempt seems to be mutiple time quicker however is still could be quicker
    print(f"There will be a total of {len(stones)} after 75 blinks.")
