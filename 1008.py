"""1008. Construct Binary Search Tree from Preorder Traversal"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        return self.dfs(preorder)

    def dfs(self, nums):
        if not nums:
            return None
        node = TreeNode(nums[0])
        nums_l = []
        nums_r = []
        for i in range(1, len(nums)):
            if nums[i] < nums[0]:
                nums_l.append(nums[i])
            else:
                nums_r.append(nums[i])
        node.left = self.dfs(nums_l)
        node.right = self.dfs(nums_r)

        return node
