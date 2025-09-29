def counting_sort(arr, exp):
    """
    A stable counting sort that sorts arr[] according to the digit represented by exp.
    exp = 1 -> sort by 1's place
    exp = 10 -> sort by 10's place
    exp = 100 -> sort by 100's place
    """
    n = len(arr)
    output = [0] * n   # output array
    count = [0] * 10   # digit range is [0-9]

    # Count occurrences of each digit
    for num in arr:
        index = (num // exp) % 10
        count[index] += 1

    # Prefix sum to transform count into position info
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build output array (iterate in reverse to keep stability)
    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    # Copy output back to arr
    for i in range(n):
        arr[i] = output[i]


def radix_sort(arr):
    # Find the maximum number to know the number of digits
    max_num = max(arr)

    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10


# Example usage:
arr = [170, 45, 75, 90, 802, 24, 2, 66]
radix_sort(arr)
print("Sorted array:", arr)
