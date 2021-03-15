"""100. Same Tree"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        return self.dfs(p, q)
    def dfs(self, p, q):
        if not p and not q:
            return True
        elif not p or not q:
            return False
        elif p.val != q.val: # !! has to write this after deciding they are not None
            return False
        return self.dfs(p.left, q.left) and self.dfs(q.right, p.right)
