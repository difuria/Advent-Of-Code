from Inputs.puzzle_inputs import puzzle_input
from Inputs.test_inputs import test_input_1


def generate_blocks(text: str) -> list[str]:
    blocks = []
    for i in range(0, len(text), 2):
        index = i // 2
        blocks += [str(index)] * int(text[i])
        free_blocks = i+1
        if free_blocks < len(text):
            blocks += ["."] * int(text[i+1])
    
    return blocks


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


def calculate_checksum(blocks: list[str]) -> None:
    check_sum = 0
    for i in range(len(blocks)):
        if blocks[i] == ".":
            continue

        check_sum += (i * int(blocks[i]))

    print(f"Checksum is {check_sum}")


print("Task 1")
blocks = generate_blocks(test_input_1)
blocks = fill_in_block_space(blocks)
calculate_checksum(blocks)

blocks = generate_blocks(puzzle_input)
blocks = fill_in_block_space(blocks)
calculate_checksum(blocks)

print("Task 2")