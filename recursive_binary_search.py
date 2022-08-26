from .utils import sorted_numbers

def recursive_binary_search(list, target):
    if len(list) == 0:
        return False
    else:
        midpoint = (len(list)) // 2

        if list[midpoint] == target:
            return True
        elif list[midpoint] < target:
            return recursive_binary_search(list[midpoint + 1 :], target)
        else:
            return recursive_binary_search(list[: midpoint + 1], target)


def verify(index):
    if index is not None:
        print("Value found: ", index)
    else:
        print(f"Value not found: {index}")


result = recursive_binary_search(sorted_numbers, 11)
verify(result)
