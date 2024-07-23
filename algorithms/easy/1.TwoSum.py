class Solution:

    """
    Given an array of integers nums and an integer target, return indices of the two numbers 
    such that they add up to target. You may assume that each input would have exactly one 
    solution, and you may not use the same element twice. You can return the answer in any order.
    """

    def twoSum1(self, nums: list[int], target: int) -> list[int]:
        # brute force solution O(N^2)
        for i in range(len(nums) - 1):
            
            for j in range(i+1, len(nums)):
                
                if nums[i] + nums[j] == target:
                    return [i, j]
                    # break
def two_sum(nums, target):
    # O(N) solution
    hm = {}
    for i, n in enumerate(nums):
        
        diff = target - n
        
        if diff in hm:
            
            return [hm[diff], i]
        hm[n] = i
        print
    return []

def two_sum1(nums: list, target: int):
    # O(N) 
    hm = {}
    current_number, second_index = -100, -100
    for i in range(len(nums)):
        # print('i is', i, 'nums[i] is', nums[i])
        current_number = nums[i]
        diff = target - current_number
        # print('diff is', diff)
        if current_number in hm.keys():
            second_index = i
            break
        else:
            hm[diff] = i
    if current_number == -100 or second_index == -100:
        return []
    else:
        return [hm[current_number], second_index]



if __name__=="__main__":
    # a = Solution()
    # print(a.twoSum([7, 8, 2, 11, 3, 4, 5], 6))
    # print(a.twoSum1([3, 2, 4], 6))

    print(two_sum([5, 1, 7, 2, 9, 3], 10))  
    print(two_sum([4, 2, 11, 7, 6, 3], 9))  
    print(two_sum([10, 15, 5, 2, 8, 1, 7], 12))  
    print(two_sum([1, 3, 5, 7, 9], 10))  
    print ( two_sum([1, 2, 3, 4, 5], 10) )
    print ( two_sum([1, 2, 3, 4, 5], 7) )
    print ( two_sum([1, 2, 3, 4, 5], 3) )
    print ( two_sum([], 0) )