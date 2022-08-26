from .utils import unsorted_numbers


def merge_sort(value):
    if len(value) <= 1:
        return value
    midpoint = len(value) // 2
    left_half = merge_sort(value[:midpoint])
    right_half = merge_sort(value[midpoint:])
    sorted_list = []
    left_index = 0
    right_index = 0
    while left_index < len(left_half) and right_index < len(right_half):
        if left_half[left_index] < right_half[right_index]:
            sorted_list.append(left_half[left_index])
            left_index += 1
        else:
            sorted_list.append(right_half[right_index])
            right_index += 1
    sorted_list += left_half[left_index:]
    sorted_list += right_half[right_index:]
    return sorted_list


print(f"unsorted list: {unsorted_numbers}")
sorted_list = merge_sort(unsorted_numbers)
print(f"sorted list: {sorted_list}")
