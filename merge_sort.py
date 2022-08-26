from .utils import unsorted_numbers


def merge_sort(list):

    if len(list) <= 1:
        return list

    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)


def split(list):
    """
    Divide the unsorted list at
    midpoint into sublists.
    Returns two sublists - left and right
    """
    mid = len(list) // 2
    left = list[:mid]
    right = list[mid:]
    return left, right


def merge(left, right):
    """
    Merge two lists, sorting them in the process
    Returns a new merged list
    """
    l = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1

    while i < len(left):
        l.append(left[i])
        i += 1

    while j < len(right):
        l.append(right[j])
        j += 1
    return l


sorted_merge = merge_sort(unsorted_numbers)
print(sorted_merge)


def verify_sort(list):
    if len(list) <= 1:
        return True
    return list[0] < list[1] and verify_sort(list[1:])


print(verify_sort(unsorted_numbers))
print(verify_sort(sorted_merge))
