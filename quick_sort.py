from .utils import unsorted_numbers
def quick_sort(value):
    if len(value) <= 1:
        return value
    lesser_than_pivot = []
    greater_than_pivot = []
    pivot = value[0]
    for value in value[1:]:
        print(f"pivot: {pivot}")
        if value < pivot:
            lesser_than_pivot.append(value)
        else:
            greater_than_pivot.append(value)
    return quick_sort(lesser_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

sorted_array = quick_sort(unsorted_numbers)
print(sorted_array)
