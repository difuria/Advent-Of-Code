from Inputs.puzzle_inputs import puzzle_input_1
from Inputs.test_inputs import test_input


def blink_stones_inplace(text: str, blinks: int) -> list[int]:
    """
    Solution edits and stores the stones in place. Very slow and poor memory efficency. 
    """
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


# Store a cache of the stones and the steps we've seen previously. 
memory = {}
def count(stone: int, steps: int) -> int:
    if steps == 0:
        return 1
    
    key = (stone, steps)
    if key in memory:
        return memory[key]

    steps -= 1
    if stone == 0:
        memory[key] = count(1, steps)
    elif len(str(stone)) % 2 == 0:
        str_stone = str(stone)
        stone_length = len(str_stone)
        left, right = str_stone[:stone_length//2], str_stone[stone_length//2:]
        memory[key] = count(int(left), steps) + count(int(right), steps)
    else:
        memory[key] = count(stone * 2024, steps)
    
    return memory[key]


def blink_stones(text: str, blinks: int) -> list[int]:
    """
    As we calculate the stone on the final blink we can discard it.
    Much faster and very little memory. However still too slow for 75 blinks.
    """
    memory = {}
    stones = list(map(int, text.strip().split()))

    number_of_stones = 0
    for stone in stones:
        number_of_stones += count(stone, blinks)

    return number_of_stones


print("Test Inputs")
test_count = 0
passed = 0
for test in ["1", "2"]:
    test_count += 1
    print(f"Test {test}.")
    stones = blink_stones(test_input[test]["Input"]["stones"], test_input[test]["Input"]["blinks"])
    print(f"There are now {stones}")
    if stones == len(test_input[test]["Answers"]["Task 1"]["output"].split()):
        passed += 1
        print(f"passed")
    else:
        print(f"failed")

if passed == test_count:
    print("\nAll test cases passed, running puzzle input.")
    stone_count = blink_stones(puzzle_input_1, 25)
    print(f"There will be a total of {stone_count} after 25 blinks.")
    blinks = 75
    stone_count = blink_stones(puzzle_input_1, blinks) # This attempt seems to be mutiple time quicker however it still could be quicker
    print(f"There will be a total of {stone_count} after {blinks} blinks.")
