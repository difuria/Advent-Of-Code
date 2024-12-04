import hashlib
import re

def get_hash(key: str, string_to_match: str) -> str:
    i = 0
    while True:
        hash = hashlib.md5(f"{key}{i}".encode()).hexdigest()
        if re.match(string_to_match, hash):
            return i

        i += 1

print("Task 1")
keys = ["abcdef", "pqrstuv", "bgvyzdsv"]
match = r"^0{5}"
for key in keys:
    print(f"Number to secret {key} of is {get_hash(key, match)} for match of {match}.")

print("\nTask 2")
keys = ["abcdef", "pqrstuv", "bgvyzdsv"]
match = r"^0{6}"
for key in keys:
    print(f"Number to secret {key} of is {get_hash(key, match)} for match of {match}.")