from Inputs.puzzle_inputs import puzzle_input
from Inputs.test_inputs import test_input_1, test_answer_1_1, test_answer_1_2


def generate_blocks(text: str) -> tuple[list[str], list[dict[str, any]], list[dict[str, any]]]:
    blocks = []
    block_spaces = []
    free_spaces = [] # Idea is to have the index and number of free spaces remaining
    for i in range(0, len(text), 2):
        index = i // 2

        block_spaces.append({ 
            "starting index": len(blocks), 
            "id": str(index),
            "length": int(text[i])
        })

        blocks += [str(index)] * int(text[i])

        free_blocks = i+1
        if free_blocks < len(text):
            free_spaces.append({
                "starting index": len(blocks), 
                "length": int(text[free_blocks])
            })
            blocks += ["."] * int(text[free_blocks])
    
    return blocks, block_spaces, free_spaces


def fill_in_block_space(blocks: list[str]) -> list[str]:
    left = 0
    right = len(blocks) - 1

    while left < right:
        if blocks[left] == ".":
            if blocks[right] != ".":
                blocks[left] = blocks[right]
                blocks[right] = "."
                left += 1
            else:
                right -= 1
        else:
            left += 1
    
    return blocks


def fill_in_block_space_whole(
        blocks: list[str], 
        block_spaces: list[dict[str, any]], 
        free_spaces: list[dict[str, any]]
        ) -> list[str]:

    # Just loop through the block sizes and free space sizes instead of continuously looping through the blocks.
    while block_spaces:
        block_space = block_spaces.pop()

        for i, free_space in enumerate(free_spaces):
            # Once the blocks meets the free space index we know we've looped through everything
            if block_space["starting index"] <= free_space["starting index"]:
                break

            if block_space["length"] <= free_space["length"]:
                right = block_space["starting index"]
                for left in range(free_space["starting index"], free_space["starting index"] + block_space["length"]):
                    blocks[left] = blocks[right]
                    blocks[right] = "."
                    right += 1

                free_space["starting index"] = left + 1
                free_space["length"] -= block_space["length"]

                if free_space["length"] == 0:
                    free_spaces.pop(i)

                break

    return blocks


def calculate_checksum(blocks: list[str]) -> int:
    check_sum = 0
    for i in range(len(blocks)):
        if blocks[i] == ".":
            continue

        check_sum += (i * int(blocks[i]))

    print(f"Checksum is {check_sum}")
    return check_sum


print("Task 1")
blocks, block_spaces, free_spaces = generate_blocks(test_input_1)
blocks = fill_in_block_space(blocks)
check_sum = calculate_checksum(blocks)

if check_sum == test_answer_1_1:
    blocks, block_spaces, free_spaces = generate_blocks(puzzle_input)
    blocks = fill_in_block_space(blocks)
    calculate_checksum(blocks)

print("\nTask 2")
blocks, block_spaces, free_spaces = generate_blocks(test_input_1)
blocks = fill_in_block_space_whole(blocks, block_spaces, free_spaces)
check_sum = calculate_checksum(blocks)

if check_sum == test_answer_1_2:
    blocks, block_spaces, free_spaces = generate_blocks(puzzle_input)
    blocks = fill_in_block_space_whole(blocks, block_spaces, free_spaces)
    calculate_checksum(blocks)