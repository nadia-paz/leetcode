
import random
import heapq
"""
Find Kth-smallest and Kth-largest numbers in the list without sorting. Not distinct element
a) with heap
b" with Quick Search algorithm
"""

def find_kth_largest(nums: list, k: int):
    if len(nums) == 0 or len(nums) < k:
        return None
    
    # pick a random element of the array
    rand = random.choice(nums)

    # break values < and > than random
    left =  [x for x in nums if x > rand]
    mid  =  [x for x in nums if x == rand]
    right = [x for x in nums if x < rand]

    L, M = len(left), len(mid)
    
    if k <= L:
        # if the length of the left array bigger or equal to k
        return find_kth_largest(left, k)
    elif k > L + M:
        # if the length of the k bigger then length of the left+mid
        # than the value can't be in left or mid array
        return find_kth_largest(right, k - L - M)
    else:
        # than kth largest is located in mid array and equals to the random number
        return mid[0]

def find_kth_smallest(nums:list, k:int):
    if len(nums) == 0 or len(nums) < k:
        return None

    rand = random.choice(nums)
    # rand = nums[k//2]
    # print(rand)

    left = [x for x in nums if x < rand]
    mid = [x for x in nums if x == rand]
    right = [x for x in nums if x > rand]
    # print("Left:", left)
    # print("Mid:", mid)
    # print("Right:", right)
    L, M = len(left), len(mid)

    if k <= L:
        # print("left, k=", k)
        # print("\n\n\n")
        return find_kth_smallest(left, k)
    elif k > L + M:
        # print("right, k=", k - L - M)
        # print("\n\n\n")
        return find_kth_smallest(right, k - L - M)
    else: 
        # print("Final mid:", mid)
        return mid[0]




nums = [45, 36, 3, 33, 12, 1, 2, 90, 123, -3, 12, 56, 78, 52, 19]
# nums = [45, 36, 3, 33, 12, 1, 2, 90]

# Tests:
nums1 = nums.copy()
nums1.sort()
for k in range(1, len(nums)+1):
    print("k = ", k)
    try:
        result = find_kth_largest(nums, k)
        assert  result == nums1[-k]
        print("Kth largest pass, k =", k, "result = ", result)
    except:
        print("Kth largest fail, k =", k, "result = ", result)
    try:
        result = find_kth_smallest(nums, k)
        assert result == nums1[k-1]
        print("Kth smallest pass, k =", k, "result = ", result)
    except:
        print("Kth smallest fail, k=",k, "result = ", result)
    print("**************\n")