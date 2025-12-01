import os

script_dir: str  = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(script_dir, "Inputs", "test_input.txt"), "r") as f:
    test_inputs: list[str] = [line.strip() for line in f.read().strip().splitlines()] 


with open(os.path.join(script_dir, "Inputs", "puzzle_input.txt"), "r") as f:
    puzzle_inputs: list[str] = [line.strip() for line in f.read().strip().splitlines()] 

def calculate(strings: list[str]) -> int:
    total: int = 0
    for string in strings:
        total_length: int = len(string)
        char_count: int = 0
        char_index: int = 1
        while char_index < total_length - 1:
            if string[char_index] != "\\":
                char_count += 1
                char_index += 1
            else:
                char_index += 1
                if string[char_index] == "x":
                    char_index += 2
                elif string[char_index] == "\\":
                    char_index += 1
                    char_count += 1

        total += (total_length - char_count)

    return total

def encode(strings: list[str]) -> list[str]:
    for index, string in enumerate(strings):
        current: list[str] = ["\""]
        for char in string:
            if char in ["\"", "\\"]:
                current.append("\\")
            current.append(char)
            
        current.append("\"")

        strings[index] = "".join(current)
    
    return strings

def calculate_difference(original: list[str], encoded: list[str]) -> int:
    total: int = 0
    for index, og_string in enumerate(original):
        total += (len(encoded[index]) - len(og_string))
    
    return total


print("Part 1")
print("Test total", calculate(test_inputs))
print("Puzzle total", calculate(puzzle_inputs))

print("Part 2")
print("Test total", calculate_difference(test_inputs, encode(test_inputs[:])))
print("Puzzle total", calculate_difference(puzzle_inputs, encode(puzzle_inputs[:])))