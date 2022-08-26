def sum(numbers):
    """
    iteration
    """
    total = 0
    for number in numbers:
        total += number
    return total

def sum(numbers):
    """
    recursive
    """
    if not numbers:
        return 0
    remaining_sum = sum(numbers[1:])
    return numbers[0] + remaining_sum
