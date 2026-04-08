def get_unique(numbers):
    unique = []
    for num in numbers:
        if num not in unique:
            unique.append(num)
    return unique
