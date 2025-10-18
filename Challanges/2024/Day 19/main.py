from Inputs.puzzle_inputs import puzzle_input_1
from Inputs.test_inputs import test_input_1


def get_towels(text: str) -> tuple[set[str], list[str], int]:
    towel_input: list[str] = text.strip().split("\n\n")

    longest_towel: int = 0
    possible_towels: set[str] = set()
    for towel in towel_input[0].split(","):
        towel = towel.strip()
        possible_towels.add(towel)
        longest_towel = max(longest_towel, len(towel))

    potential_towels: list[str] = towel_input[1].strip().split("\n")

    return possible_towels, potential_towels, longest_towel


def find_towels(puzzle_input: str) -> int:
    possible_towels, potential_towels, longest_towel = get_towels(puzzle_input)

    possible: int = 0
    for potential_towel in potential_towels:
        stack: list[int] = [0]

        while stack:
            index: int = stack.pop()

            if index == len(potential_towel):
                possible += 1
                break
            
            if index < len(potential_towel):
                for i in range(0, longest_towel):
                    end_index: int = index+i+1
                    if end_index <= len(potential_towel) and potential_towel[index:end_index] in possible_towels:
                        stack.append(end_index)

    print(f"There are {possible} possible towel sequences.")


def find_towels_all_combinations(puzzle_input: str) -> int:
    possible_towels, potential_towels, longest_towel = get_towels(puzzle_input)

    # Need to change to be recursive to add a mapping

    possible: int = 0
    for potential_towel in potential_towels:

        seen: dict[int, int] = {}
        def is_possible(index: int) -> int:
            nonlocal potential_towel
            nonlocal longest_towel
            nonlocal possible
            nonlocal seen

            if index in seen:
                return seen[index]
            elif index == len(potential_towel):
                # possible += 1
                return 1
            elif index > len(potential_towel):
                return False
            
            possibilities = 0
            for i in range(0, longest_towel):
                end_index: int = index+i+1
                if end_index <= len(potential_towel) and potential_towel[index:end_index] in possible_towels:
                    possibilities += is_possible(end_index)
            
            if index not in seen:
                seen[index] = possibilities
            
            return seen[index]
        
        is_possible(0)
        possible += seen[0]
    
    print(f"There are a total of {possible} towel combinations.")


possible_sequences: int = find_towels(test_input_1)
possible_sequences: int = find_towels(puzzle_input_1)

possible_sequences: int = find_towels_all_combinations(test_input_1)
possible_sequences: int = find_towels_all_combinations(puzzle_input_1)