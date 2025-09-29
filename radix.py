def radix_sort(nums) -> list:
    n = len(nums)
    output = [0] * n #output array
    count = [0] * 10 # digits 0-9

    print(f'output: {output}, count: {count}')


if __name__ == "__main__":
    nums = [523, 52, 641, 74, 7, 540, 32, 7809]
    radix_sort(nums)