"""156. Binary Tree Upside Down"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root or not root.left:
            return root
        futureRoot = self.upsideDownBinaryTree(root.left)
        rMost = futureRoot
        while rMost.right:
            rMost = rMost.right

        root, rMost.left, rMost.right = futureRoot, root.right, TreeNode(root.val)

        return root
