def valid_password(password, task):
    password = str(password)

    if len(password) != 6 or not password.isdigit():
        return False
    
    current_value = -1
    adjacent_digits = False
    running_lengths = {}
    for digit in password:
        digit = int(digit)
        if digit < current_value:
            return False
        elif digit == current_value:
            adjacent_digits = True
            if not digit in running_lengths:
                running_lengths[digit] = 1
            running_lengths[digit] += 1

        current_value = digit

    if task == 2:
        if running_lengths:
            contains_double = False
            for value in running_lengths.values():
                if value == 2:
                    contains_double = True
            
            return contains_double

    return adjacent_digits

if __name__ == "__main__":
    task = 2
    for password in ["122345", "111123", "135679", "111111", "223450", "123789", "112233", "123444", "111122"]:
        valid = valid_password(password, task)
        print(f"{password} is valid {valid}")

    from_val, to_val = [138241, 674034]
    print(f"\nPuzzle range {from_val} to {to_val}")
    valid_passwords = 0
    for password in range(from_val, to_val):
        if valid_password(password, task):
            valid_passwords += 1
    
    print(f"There are {valid_passwords} valid passwords.")
