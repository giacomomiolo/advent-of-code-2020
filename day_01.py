from typing import List
import math # requires python 3.8+ for prod function

test_input = [
    1721,
    979,
    366,
    299,
    675,
    1456
]

def two_sum_prod(input_ls: List[int]) -> int:
    """
    Find the two entries that sum to 2020
    and then multiply those two numbers together.
    Two Sum problem, O(n) solution using hashmap.
    """
    complement = {2020 - i for i in input_ls}
    
    for i in input_ls:
        if i in complement:
            return i * (2020 - i)

def three_sum(nums: List[int], sum_to: int = 2020) -> int:
    """
    Find the product of the three entries that sum to 2020, same data.
    """
    results = []
    nums.sort()

    for i, a in enumerate(nums):
        if i > 0 and a == nums[i - 1]:
            continue
        
        l, r = i + 1, len(nums) - 1
        while l < r:
            three_sum = a + nums[l] + nums[r]
            if three_sum > sum_to:
                r -= 1
            elif three_sum < sum_to:
                l += 1
            else:
                results.append([a, nums[l], nums[r]])
                l += 1
                while nums[l] == nums[l - 1] and l < r:
                    l += 1
    return results

# Tests
assert two_sum_prod(test_input) == 514579
assert math.prod(three_sum(test_input)[0]) == 241861950

with open("data/input_01.txt", "r") as f:
    inputs = [int(line) for line in f]
    print(f"Product of two numbers that sum to 2020: {two_sum_prod(inputs)}")
    print(f"Three numbers that sum to 2020: {three_sum(inputs)}")
    print(f"Product: {math.prod(three_sum(inputs)[0])}")