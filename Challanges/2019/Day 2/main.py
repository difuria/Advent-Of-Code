import os, sys

def analyse_program(program, output = True):
    index = 0
    while index < len(program):
        item = program[index]
        if item == 99:
            break
        elif item in [1, 2]:
            first_location = program[index+1]
            second_location = program[index+2]
            answer_locaion = program[index+3]

            if item == 1:
                program[answer_locaion] = program[first_location] + program[second_location]
            elif item == 2:
                program[answer_locaion] = program[first_location] * program[second_location]
            
        index += 4
    
    if output:
        print(f"Value at position 0 is {program[0]}")
    return program[0]

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

    for i in range(1, 6):
        program = get_file(path, f"test_program_{i}.txt")
        program = list(map(int, program.strip().split(",")))
        analyse_program(program)
    
    program = get_file(path, f"puzzle_program_1.txt")
    program = list(map(int, program.strip().split(",")))
    program[1] = 12
    program[2] = 2
    analyse_program(program)

    program = get_file(path, f"puzzle_program_1.txt")
    program = list(map(int, program.strip().split(",")))
    for noun in range(100):
        for verb in range(100):
            current_program = program[:]
            current_program[1] = noun
            current_program[2] = verb

            output = analyse_program(current_program, False)

            if output == 19690720:
                print(f"Noun was {noun}, verb was {verb} answer is {(100*noun)+verb}")
