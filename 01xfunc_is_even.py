def is_even(arr):
    if not arr:
        raise ValueError("This input array cannot be empty")
    even_count = 0
    for num in arr:
        if num % 2 == 0:
            even_count += 1
    return even_count
result = is_even([1, 2, 3, 4, 5, 6])
print(f"Count of even numbers: {result}")