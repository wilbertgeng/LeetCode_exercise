"""654. Maximum Binary Tree"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        ## preorder 
        return self.dfs(nums)

    def dfs(self, nums):
        if not nums:
            return None
        max_v = float('-inf')
        idx = 0
        for i in range(len(nums)):
            if nums[i] > max_v:
                max_v = nums[i]
                idx = i

        root = TreeNode(nums[idx])
        root.left = self.dfs(nums[0:idx])
        root.right = self.dfs(nums[idx+1:])

        return root
