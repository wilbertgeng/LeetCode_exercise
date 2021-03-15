"""701. Insert into a Binary Search Tree"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        ## corner case if input is an empty []
        if not root:
            return TreeNode(val)

        if root.val < val:
            if not root.right:
                root.right = TreeNode(val)
            else:
                root.right = self.insertIntoBST(root.right, val)

        elif root.val > val:
            if not root.left:
                root.left = TreeNode(val)
            else:
                root.left = self.insertIntoBST(root.left, val)

        else:
            return root

        return root
