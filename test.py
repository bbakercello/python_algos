from typing import Counter, List


def bag_counter(numbers: List) -> int:
    '''
    This function finds the largest sum of pairs with equal sum.
    
    Args:
        numbers: A list of integers to find pairs from
        
    Returns:
        int: The maximum number of pairs that can be formed with equal sums
    '''
    bag = Counter(numbers)

    min_sum = 2 # smallest possible pair sum (1+1)
    max_sum = 2 * max(numbers)
    best = 0

    # For each sum
    for s in range(min_sum, max_sum + 1):
        temp_bag = bag.copy()
        pairs = 0
       
       # For each key value in temp_bag
        for x, count in temp_bag.items():
            y = s - x
            if y not in temp_bag:
                continue # can't form this pair
            if x == y:
                pairs += count // 2 # how many pairs of this number are at this key
                temp_bag[x] = 0
            else:
                available = min(temp_bag[x], temp_bag[y])
                pairs += available
                temp_bag[x] = 0
                temp_bag[y] = 0
        best = max(best, pairs)
    return best


if __name__ == "__main__":

    # Each one of these numbers represents a singular item (and it's weight)
    test_numbers = [1,1,3,4,5,6,7,1,2,3,5]

    bag_result = bag_counter(test_numbers)
    print(f'Here is the largest number of pairs equaling the same sum: {bag_result}')
