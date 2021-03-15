"""538. Convert BST to Greater Tree"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        ######
        self.sum = 0
        return self.dfs(root)
    def dfs(self, node):
        if not node:
            return None
        self.dfs(node.right)
        self.sum += node.val
        node.val = self.sum
        self.dfs(node.left)
        return node

#######
        self.res = 0
        self.dfs(root)

        return root

    def dfs(self, node):
        if not node:
            return

        node.right = self.dfs(node.right)
        self.res += node.val
        node.val = self.res
        node.left = self.dfs(node.left)

        return node
