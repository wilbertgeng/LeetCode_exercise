"""226. Invert Binary Tree
Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        ############# Practice:

        return self.dfs(root)
    def dfs(self, node):
        if not node:
            return None
        node.left ,node.right = self.dfs(node.right), self.dfs(node.left)
        return node
    
        ############# Practice
        return self.invert(root)

    def invert(self, node):
        if not node:
            return None
        left = self.invert(node.right)
        right = self.invert(node.left)

        node.left = left
        node.right = right

        return node
        ##############
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
