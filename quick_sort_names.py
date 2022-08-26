from .utils import unsorted_names


def quick_sort(value):
    if len(value) <= 1:
        return value
    lesser_than_pivot = []
    greater_than_pivot = []
    pivot = value[0]
    for value in value[1:]:
        if value < pivot:
            lesser_than_pivot.append(value)
        else:
            greater_than_pivot.append(value)
    return quick_sort(lesser_than_pivot) + [pivot] + quick_sort(greater_than_pivot)



sorted_names = quick_sort(unsorted_names)
for names in sorted_names:
    print(names)
