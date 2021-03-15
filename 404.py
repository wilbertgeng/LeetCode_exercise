"""404. Sum of Left Leaves"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ######### Practice:
        self.res = 0
        if not root:
            return 0
        self.dfs(root)
        return self.res
    def dfs(self, root):
        if not root:
            return
        if root.left and not root.left.left and not root.left.right:
            self.res += root.left.val
        self.dfs(root.left)
        self.dfs(root.right)

            
        ###########
        if not root: ##exit condition
            return 0

        if root.left and not root.left.left and not root.left.right:
            return root.left.val + self.sumOfLeftLeaves(root.right)

        return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
