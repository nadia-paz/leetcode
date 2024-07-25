"""
Given an unsorted array of integers, write a function that finds the length of the  
longest_consecutive_sequence (i.e., sequence of integers in which each element
is one greater than the previous element).
"""

def longest_consecutive_sequence(nums):
    n_set = set(nums)
    # nums.sort()
    
    max_ = 0
    for n in nums:
        # do only if the number wasn't a part of a seq before
        if n-1 not in n_set:
            curr = n 
            seq_len = 1 
            while curr+1 in n_set:
                curr += 1
                seq_len += 1 
            max_ = seq_len if seq_len > max_ else max_
    return max_

print( longest_consecutive_sequence([100, 4, 5, 0, -1, 200, 1, 3, 2]) ) #7

