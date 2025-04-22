def sanitize_list(lst, index=0):
    if index == len(lst):
        return
    if lst[index] < 0:
        lst[index] = 0
    sanitize_list(lst, index + 1)

# Example usage
numbers = [5, -3, 7, -1, 0, -8, 4]
sanitize_list(numbers)
print("Sanitized list:", numbers)
