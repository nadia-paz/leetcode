# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        
        left = 0
        right = len(nums)
        if len(nums) == 0:
            return None
        med = len(nums) // 2
        # node = Node(nums[med])
        node = TreeNode(nums[med])
        
        node.left = self.sortedArrayToBST(nums[left:med])
        node.right = self.sortedArrayToBST(nums[med+1:right])
        return node