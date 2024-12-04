from Inputs.puzzle_inputs import puzzle_input_1
from Inputs.test_inputs import test_input_1, test_input_2

import re


def is_triangle_possible(triangle: list) -> bool:
    i, j, k = triangle
    if i + j <= k or \
       j + k <= i or \
       i + k <= j:
        return False
    return True


def horizontal_analysis(input_text: str) -> None:
    triangles = input_text.split("\n")

    count = 0
    for triangle in triangles:
        triangle = re.sub(r'\s{1,}', ' ', triangle)
        triangle = list(map(int, triangle.strip().split(" ")))

        if is_triangle_possible(triangle):
            count += 1

    print(f"There are {count} valid triangles.")


def vertical_analysis(input_text: str) -> None:
    triangles = input_text.split("\n")

    count = 0
    triangle_matrix = []
    for triangle in triangles:
        triangle_matrix.append([])
        triangle = re.sub(r'\s{1,}', ' ', triangle)
        triangle = list(map(int, triangle.strip().split(" ")))
        triangle_matrix[-1] = triangle

    count = 0
    for column in range(3):
        for row in range(0, len(triangle_matrix), 3):
            i = triangle_matrix[row][column]
            j = triangle_matrix[row+1][column]
            k = triangle_matrix[row+2][column]

            if is_triangle_possible([i, j, k]):
                count += 1
    
    print(f"There are {count} valid triangles.")


print("Task 1")
horizontal_analysis(test_input_1)
horizontal_analysis(puzzle_input_1)

print("\nTask 2")
vertical_analysis(test_input_2)
vertical_analysis(puzzle_input_1)
