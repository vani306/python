def average_recursive(lst, index=0, total=0):
    if index == len(lst):
        return total / len(lst) if len(lst) > 0 else 0
    return average_recursive(lst, index + 1, total + lst[index])

numbers = [10, 20, 30, 40, 50]
avg = average_recursive(numbers)
print("Average:", avg)
