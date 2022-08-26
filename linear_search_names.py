from .utils import unsorted_names


def index_of_item(collection, target):
    for i in range(0, len(collection)):
        if collection[i] == target:
            return i
    return None


for n in unsorted_names:
    index = index_of_item(unsorted_names, n)
    print(index)
