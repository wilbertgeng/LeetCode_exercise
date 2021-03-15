"""112. Path Sum"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        ### Practice:
        return self.dfs(root, targetSum)

    def dfs(self, node, target):
        if not node:
            return False
        target-=node.val
        if target == 0 and not node.left and not node.right:
            return True
        return self.dfs(node.left, target ) or self.dfs(node.right, target)











        ############# Practice
        if not root:
            return False
        if root.val == sum and root.left == None and root.right == None:
            return True
        return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val)

        ################
        if root == None:
            return False
        #### from root to leaf which is the end node
        if root.left == None and root.right == None and root.val == sum:
            return True

        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)
