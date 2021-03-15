"""108. Convert Sorted Array to Binary Search Tree"""

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
        ######## Practice:
        if not nums:
            return None
        return self.dfs(nums)
    def dfs(self, nums):
        if not nums:
            return None
        l = 0
        r = len(nums) - 1
        mid = l + (r - l)//2
        node = TreeNode(nums[mid])
        node.left = self.dfs(nums[:mid])
        node.right = self.dfs(nums[mid+1:])
        return node



        #############
        if not nums:
            return None

        n = len(nums)//2

        root = TreeNode(nums[n])
        root.left = self.sortedArrayToBST(nums[:n])
        root.right = self.sortedArrayToBST(nums[n+1:])  ### n+1

        return root
