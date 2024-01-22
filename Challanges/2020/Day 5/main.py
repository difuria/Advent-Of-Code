import os, sys

class BinaryBoarding:
    def __init__(self, passes):
        self.passes = passes.strip().splitlines()
        self.seats = []

    def get_seat_id(self):
        current_ID = -1
        for seats in self.seats:
            for seat in seats:
                if seat != None:
                    current_ID = seat
                elif current_ID != -1:
                    return current_ID + 1

    def locate_seat_pass(self, boarding_pass, rows = 128, columns = 8):
        row_range = [0, rows]
        col_range = [0, columns]

        seat = [None, None]

        for char in boarding_pass[:7]:
            row_diff = row_range[1] - row_range[0]
            row_half = row_diff // 2

            if char == "F":
                row_range[1] = row_range[0] + row_half
            else:
                row_range[0] = row_range[1] - row_half

        for char in boarding_pass[7:]:
            col_diff = col_range[1] - col_range[0]
            col_half = col_diff // 2

            if char == "L":
                col_range[1] = col_range[0] + col_half
            else:
                col_range[0] = col_range[1] - col_half
        
        seat = [row_range[0], col_range[0]]
        seat_id = (row_range[0] * 8) + col_range[0]

        self.seats[seat[0]][seat[1]] = seat_id
    
        print(f"Allocated seat is {seat}, with ID {seat_id}")
        return seat_id
        
    def find_pass_seat(self, rows = 128, columns = 8):
        self.seats = [[None][:] * columns for row in range(rows)]

        highest_seat_id = 0
        for boarding_pass in self.passes:
            highest_seat_id = max(self.locate_seat_pass(boarding_pass, rows, columns), highest_seat_id)
            
        print(f"Highest seat ID was {highest_seat_id}")
        print(f"Seat ID was {self.get_seat_id()}")

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

    binary_boarding = BinaryBoarding(get_file(path, "test_boarding_passes_1.txt"))
    binary_boarding.find_pass_seat()

    binary_boarding = BinaryBoarding(get_file(path, "puzzle_boarding_passes_1.txt"))
    binary_boarding.find_pass_seat()
