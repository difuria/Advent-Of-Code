import os, sys

input_text = "puzzle_image_1.txt"

def get_file(path, file):
    file = os.path.join(path, f"Task Inputs", file)

    if not os.path.exists(file):
        print(f"Invalid file supplied of {file}")
        sys.exit(1)

    with open(file, "r") as f:
        path_info = f.read()

    return path_info

def get_sum(digits, matching_ahead = 1):
    sum_matching = 0
    for i, digit in enumerate(digits):
        index = i + matching_ahead
        if index >= len(digits):
            index = index - len(digits)

        if digit == digits[index]:
            sum_matching += int(digit)
    
    print(f"Captcha sum {sum_matching}")

if __name__ == "__main__":
    path = os.path.dirname(__file__)

    print("Task 1")
    for j in range(1, 5):
        get_sum(get_file(path, f"test_digits_{j}.txt").strip())


    get_sum(get_file(path, f"puzzle_digits_1.txt").strip())

    print("\nTask 2")
    for j in range(5, 10):
        digits = get_file(path, f"test_digits_{j}.txt").strip()
        get_sum(digits, len(digits)//2)

    digits = get_file(path, f"puzzle_digits_1.txt").strip()
    get_sum(digits, len(digits)//2)