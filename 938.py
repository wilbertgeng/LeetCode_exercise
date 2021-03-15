"""938. Range Sum of BST"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        if not root:
            return 0
        self.res = 0
        self.dfs(root, low, high)
        return self.res
    def dfs(self, node, l, h):
        if not node:
            return
        if node.val >= l and node.val <= h:
            self.res += node.val
        self.dfs(node.left, l, h)
        self.dfs(node.right, l, h)
        



















#######
