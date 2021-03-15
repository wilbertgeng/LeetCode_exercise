"""545. Boundary of Binary Tree"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def boundaryOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def dfs_left(node):
            if not node or not node.left and not node.right:
                return
            res.append(node.val)
            if node.left:
                dfs_left(node.left)
            else:
                dfs_left(node.right)
        def dfs_leaves(node):
            if not node:
                return
            dfs_leaves(node.left)
            if node != root and not node.left and not node.right:
                res.append(node.val)
            dfs_leaves(node.right)
        def dfs_right(node):
            if not node or not node.right and not node.left:
                return

            if node.right:
                dfs_right(node.right)
            else:
                dfs_right(node.left)
            res.append(node.val) ## !! reverse order
        res = [root.val]
        dfs_left(root.left)
        dfs_leaves(root)
        dfs_right(root.right)
        return res













########
