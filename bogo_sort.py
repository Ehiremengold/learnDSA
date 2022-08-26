import random

from .utils import unsorted_numbers

def is_sorted(values):
    for index in range(len(values) - 1):
        if values[index] > values[index + 1]:
            return False
    return True


def bogo_sort(values):
    attempts = 0
    while not is_sorted(values):
        # print(attempts)
        random.shuffle(values)
        attempts += 1
    return values, attempts


print(is_sorted(unsorted_numbers))
print(bogo_sort(unsorted_numbers))
