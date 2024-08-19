
import random
import heapq
"""
Find Kth-smallest and Kth-largest numbers in the list without sorting. Not distinct element
a) with heap
b" with Quick Select algorithm
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

##### With heapq
def kth_largest_heapq(nums: list, k:int):
    heap = []
    for n in nums:
        if k > 0:
            heapq.heappush(heap, n)
            k -= 1
        else:
            heapq.heappush(heap, n)
            heapq.heappop(heap)
    return heapq.heappop(heap)

def kth_smallest_heapq(nums: list, k:int):
    # invert numbers since heapq is 
    nums_inv = [0 - x for x in nums]
    heap = []
    for n in nums_inv:
        if k > 0:
            heapq.heappush(heap, n)
            k -= 1
        else:
            heapq.heappushpop(heap, n)
    return heapq.heappop(heap) * (-1)




nums = [45, 36, 3, 33, 12, 1, 2, 90, 123, -3, 12, 56, 78, 52, 19]
# nums = [45, 36, 3, 33, 12, 1, 2, 90]
nums1 = nums.copy()
nums1.sort()
value = int(
        input(
            "Pick the function to test:\
                 \n1: find_kth_largest\
                 \n2: find_kth_smallest\
                 \n3: kth_largest_heapq,\
                 \n4: kth_smallest_heapq\n"
            )
        )
# Tests:
if value == 1:
    # print("k = ", k)
    for k in range(1, len(nums)+1):
        # print("find_kth_largest")
        try:
            result = find_kth_largest(nums, k)
            assert  result == nums1[-k]
            print("Pass, k =", k, "result = ", result)
        except:
            print("Fail, k =", k, "result = ", result)
elif value == 2:
    for k in range(1, len(nums)+1):
        try:
            result = find_kth_smallest(nums, k)
            assert result == nums1[k-1]
            print("Pass, k =", k, "result = ", result)
        except:
            print("Fail, k=",k, "result = ", result)
elif value == 3:
    for k in range(1, len(nums)+1):
        try:
            result = kth_largest_heapq(nums, k)
            assert result == heapq.nlargest(k, nums)[k-1]
            print("Pass, k =", k, "result = ", result)
        except:
            print("Fail, k=",k, "result = ", result)
else:
    for k in range(1, len(nums)+1):
        try:
            result = kth_smallest_heapq(nums, k)
            assert result == heapq.nsmallest(k, nums)[k-1]
            print("Pass, k =", k, "result = ", result)
        except:
            print("Fail, k=",k, "result = ", result)