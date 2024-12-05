from Inputs.puzzle_inputs import puzzle_input_1
from Inputs.test_inputs import test_input_1


def split_instructions(text: str) -> list:
    ordering_instructions, pages = text.strip().split("\n\n")

    instructions = {}
    for instruction in ordering_instructions.split("\n"):
        i = list(map(int, instruction.split("|")))
        if i[0] not in instructions:
            instructions[i[0]] = set()
        
        instructions[i[0]].add(i[1])

    updates = []
    for ps in pages.split("\n"):
        updates.append(list(map(int, ps.strip().split(","))))
    
    return instructions, updates


def order_pages(updates: list, ordering_instructions: dict) -> list:
    ordered_pages = []
    for update in updates:
        ordered_pages.append([])
        for page in update:
            index = 0
            while index < len(ordered_pages[-1]):
                op = ordered_pages[-1][index]
                if page in ordering_instructions and op in ordering_instructions[page]:
                    ordered_pages[-1].insert(index, page)
                    page = None
                    break
                index += 1

            if page:
                ordered_pages[-1].append(page)
    
    return ordered_pages


def count_mid(ordered_pages: list) -> None:
    middle_count = 0
    for pages in ordered_pages:
        if len(pages) == 0:
            continue
        if len(pages) == 1:
            middle_count += pages[0]
            continue

        mid = len(pages) // 2
        middle_count += pages[mid]

    print(f"Middle count is {middle_count}")


def is_valid_order(page_locations: dict, ordering_instructions: dict) -> bool:
    for first, seconds in ordering_instructions.items():
        for second in seconds:
            if first in page_locations and second in page_locations and page_locations[first] > page_locations[second]:
                return False
    
    return True


def get_sorted_orders(ordering_instructions: dict, updates: list) -> list:
    pre_sorted_orders = []
    un_sorted_orders = []
    for update in updates:
        pages_locations = {}
        for index, page in enumerate(update):
            pages_locations[page] = index
        
        if is_valid_order(pages_locations, ordering_instructions):
            pre_sorted_orders.append(update)
        else:
            un_sorted_orders.append(update)

    return pre_sorted_orders, un_sorted_orders


print("Test Input")
ordering_instructions, orders = split_instructions(test_input_1)
pre_sorted_orders, un_sorted_orders = get_sorted_orders(ordering_instructions, orders)
print("Task 1")
count_mid(pre_sorted_orders)
ordered_pages= order_pages(orders, ordering_instructions)
print("Task 2")
count_mid(ordered_pages)

print("\nPuzzle Input")
ordering_instructions, orders = split_instructions(puzzle_input_1)
pre_sorted_orders, un_sorted_orders = get_sorted_orders(ordering_instructions, orders)
print("Task 1")
count_mid(pre_sorted_orders)
ordered_pages = order_pages(un_sorted_orders, ordering_instructions)
print("Task 2")
count_mid(ordered_pages)