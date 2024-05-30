def median(l):
    # l -> sorted list
    # O(1)
    n = len(l)
    return (
        # create a tuple and pick 1st element if even, 2nd if odd
        (l[n//2 - 1] + l[n//2]) / 2.0,
        l[n//2]
        )[n%2] if n else None

def merge_sorted_lists(nums1, nums2):
    # O(m+n)
    m, n = len(nums1), len(nums2)

    # merged list at the moment filled with zeros
    merged_nums = [0] * (m + n)
    # i -> index tracking for nums1
    # j -> index tracking for nums2
    # k -> index tracking for merded_nums
    i, j, k = 0, 0, 0
    
    while i < m and j < n:
        # pick the minimum and assign to merged_nums
        if nums1[i] <= nums2[j]:
            merged_nums[k] = nums1[i]
            i += 1
        else:
            merged_nums[k] = nums2[j]
            j += 1
        k += 1
    
    # if there are still left elements in the lists, add them to the merged_nums
    while k != (m + n):
        if i < m:
            merged_nums[k] = nums1[i]
            i += 1
            k += 1
        if j < n:
            merged_nums[k] = nums2[j]
            j += 1
            k += 1
    return merged_nums

# class Solution:
def findMedianSortedArrays1(nums1: list[int], nums2: list[int]) -> float:
    # O(m+n)
    merged = merge_sorted_lists(nums1, nums2)
    print(merged)
    return median(merged)

a = [5, 6, 8, 9, 10, 35, 44]
b = [9, 25, 67, 77, 87, 99, 101]

print(findMedianSortedArrays1(a, b))
    



        

