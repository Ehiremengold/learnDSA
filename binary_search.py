from .utils import sorted_numbers


def binary_search(list, target):
    first_position = 0  # first position
    last_position = len(list) - 1  # last position

    while first_position <= last_position:
        midpoint = first_position + last_position // 2
        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first_position = midpoint + 1
        else:
            last_position = midpoint - 1
    return None


def verify(index):
    if index is not None:
        print(f"Found at index: {index}")
    else:
        print("Value not found")


result = binary_search(sorted_numbers, 4)
verify(result)
