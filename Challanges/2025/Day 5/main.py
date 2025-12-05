from Inputs.test import t1
from Inputs.puzzle import p1


def count_fresh_ingredients(database: str) -> int:
    _ranges, ingredients = database.strip().split("\n\n")

    seen: dict[int, int] = {}

    db_ranges: list[list[int]] = []
    for _range in _ranges.strip().splitlines():
        db_ranges.append(list(map(int, _range.split("-"))))

    fresh_count: int = 0
    for ingredient in ingredients.strip().splitlines():
        ingredient = int(ingredient)

        if ingredient not in seen:
            for start, end in db_ranges:
                if ingredient >= start and ingredient <= end:
                    seen[ingredient] = 1
                    break

            if ingredient not in seen:
                seen[ingredient] = 0

        fresh_count += seen[ingredient] 

    return fresh_count


def determine_all_possible_fresh_ingredients(database: str) -> int:
    _ranges, ingredients = database.strip().split("\n\n")
    
    db_ranges: list[list[int]] = []
    for _range in _ranges.strip().splitlines():
        db_ranges.append(list(map(int, _range.split("-"))))

    combined_ranges: list[list[int]] = []

    while db_ranges:
        start, end = db_ranges.pop()

        changes: bool = True
        while changes:
            changes = False
            for index, db_range in enumerate(db_ranges):
                cs, ce = db_range

                if (start >= cs and start <= ce) or (end >= cs and end <= ce) or (cs >= start and cs <= end) or (ce >= start and ce <= end):
                    start = min(start, cs)
                    end = max(end, ce)
                    db_ranges.pop(index)
                    changes = True

        combined_ranges.append([start, end])

    fresh_count: int = 0
    for start, end in combined_ranges:
        fresh_count += (end + 1 - start)
    
    return fresh_count


print("Task 1")
print("Number of test fresh ingredients:", count_fresh_ingredients(t1))
print("Number of puzzle fresh ingredients:", count_fresh_ingredients(p1))

print("\nTask 2")
print("Total number of test fresh ingredients:", determine_all_possible_fresh_ingredients(t1))
print("Total number of puzzle fresh ingredients:", determine_all_possible_fresh_ingredients(p1))
