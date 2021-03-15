"""222. Count Complete Tree Nodes"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.dfs(root)

    def dfs(self, node):
        if not node:
            return 0

        return self.dfs(node.left) + self.dfs(node.right) + 1
