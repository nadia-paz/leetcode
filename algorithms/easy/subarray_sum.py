"""
Given an array of integers nums and a target integer target, 
write a Python function called subarray_sum that finds the indices 
of a contiguous subarray in nums that add up to the target sum 
using a hash table (dictionary).
nums = [1, 2, 3, 4, 5]
target = 9
2+3+4 = 9, so the function should return [1, 3] / [start_index, end_index]
"""

def subarray_sum(nums: list, target: int):
    # key -> sum, value -> index. 
    # value = -1 in case if the 1st element of the array=target
    sum_index = {0: -1}

    current_sum = 0

    for i, num in enumerate(nums):
        # add the number to the sum
        current_sum += num
        # calculate the difference between the current sum and the target
        diff = current_sum - target 

        if diff in sum_index:
            start = sum_index[diff] + 1
            # end = i 
            return [start, i]
        sum_index[current_sum] = i
    # if nothing found, return an empty list
    return []

nums = [1, 2, 3, 4, 5]
target = 9
print ( subarray_sum(nums, target) )

nums = [-1, 2, 3, -4, 5]
target = 0
print ( subarray_sum(nums, target) )

nums = [2, 3, 4, 5, 6]
target = 3
print ( subarray_sum(nums, target) )

nums = []
target = 0
print ( subarray_sum(nums, target) )

nums = [4, 2, 1]
target = 4 
print ( subarray_sum(nums, target) )