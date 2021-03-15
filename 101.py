"""Symmetric Tree

Given a binary tree,
check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3


But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3


Follow up: Solve it both recursively and iteratively.
"""
""" Recursive method: """
# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        ###### Practice:
        if not root:
            return True
        return self.isValid(root.left, root.right)

    def isValid(self, l, r):
        if not l and not r:
            return True
        elif not l or not r:
            return False
        elif l.val != r.val:
            return False
        return self.isValid(l.right, r.left) and self.isValid(l.left, r.right)
        #############   R2:
        if root is None: return True
        return self.isMirror(root.left, root.right)

    def isMirror(self, l, r):
        if l == None and r == None:
            return True
        if l == None or r == None:
            return False

        if l.val != r.val: return False
        #### inner outer both need to be mirrored
        return self.isMirror(l.left, r.right) and self.isMirror(l.right, r.left)










        #############  R1:
        if root is None:
            return True
        else:
            return root.isMirror(root.left, root.right)

    def isMirror(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False

        if left.val == right.val:
            inner = self.isMirror(left.right, right.left)
            outter = self.isMirror(right.right, left.left)
            return inner and outter
        else: return False
