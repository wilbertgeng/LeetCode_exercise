"""1038. Binary Search Tree to Greater Sum Tree"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.val = 0
        return self.dfs(root)
        

    def dfs(self, node):
        if node:
            self.dfs(node.right)
            self.val = node.val + self.val
            node.val = self.val
            self.dfs(node.left)

        return node
