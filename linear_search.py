from .utils import unsorted_numbers

def linear_search(list, target):
    """
    Returns the index position of the target if found,
    else return None.
    """
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None


"""
def linear_search(list, target):
    
    # recursive version of linear/sequential search
    
    if len(list) == 1:
        return False
    elif list[0] != target:
        return linear_search(list[1:], target)
    return f"found {target}"
"""


def verify(index):
    if index is not None:
        print(f"Found at index: {index}")
    else:
        print("Value not found")


result = linear_search(unsorted_numbers, 44)
verify(result)
