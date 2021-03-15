"""1026. Maximum Difference Between Node and Ancestor"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        self.dfs(root, 0, float('inf'))
        return self.res
    def dfs (self, node, max_val, min_val):
            if not node:
                self.res = max(self.res, max_val - min_val)
                return
            self.dfs(node.left, max(max_val, node.val), min(min_val, node.val))
            self.dfs(node.right, max(max_val, node.val), min(min_val, node.val))

















#########
