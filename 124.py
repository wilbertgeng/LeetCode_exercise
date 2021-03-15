"""124. Binary Tree Maximum Path Sum"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #### Practice:
        self.res = float('-inf') ## !! in case single negative node, max val can be negative
        self.dfs(root)
        return self.res

    def dfs(self, node):
        if not node:
            return 0
        left = max(0, self.dfs(node.left)) ## !! single branch can't be smaller than 0
        right = max(0, self.dfs(node.right))
        self.res = max(self.res, left + right + node.val)  ## !! update max val of a whole chain, include two branches
        return node.val + max(left, right ) ## !! return only single branch



        #######
        # post order DFS:
        self.res = float('-inf')
        self.dfs(root)
        return self.res
    def dfs(self, node):
        if not node:
            return 0
        left = max(0, self.dfs(node.left)) # don't forget max(0, ), node.val could be negative!!
        right = max(0, self.dfs(node.right))
        self.res = max(self.res, node.val + left + right) ## a single chain with two branches

        return node.val + max(left, right) ## be careful: return single branch


        #max_path = float('-inf')
        self.max_path = None
        def get_gain(node):
            #nonlocal max_path
            if node is None:
                return 0

            left_max_gain = max(get_gain(node.left), 0)
            right_max_gain = max(get_gain(node.right), 0)

            self.max_path = max(self.max_path, node.val + left_max_gain + right_max_gain)

            return node.val + max(left_max_gain, right_max_gain)

        get_gain(root)
        return self.max_path
#solution 2 similar
def maxPathSum(self, root):
    def maxend(node):
        if not node:
            return 0
        left = maxend(node.left)
        right = maxend(node.right)
        self.max = max(self.max, left + node.val + right)
        return max(node.val + max(left, right), 0)
    self.max = None
    maxend(root)
    return self.max
