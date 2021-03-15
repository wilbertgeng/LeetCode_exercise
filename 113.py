"""113. Path Sum II"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        ######## Practice:
        self.res = []
        if not root:
            return []
        self.dfs(root, sum-root.val, [root.val])
        return self.res
    def dfs(self, node, target, path):
        if not node:
            return None
        if target == 0 and not node.left and not node.right:
            self.res.append(path)
            return
        if node.left:
            self.dfs(node.left, target - node.left.val, path + [node.left.val])
        if node.right:
            self.dfs(node.right, target - node.right.val, path + [node.right.val])


        #backtracking
        self.res = []
        if not root:
            return []
        self.dfs(root, [root.val], root.val, sum)
        return self.res

    def dfs(self, node, path, pathsum, sum):
        if not node:
            return
        if pathsum == sum and not node.left and not node.right:
            self.res.append(path)
            return
        if node.left:
            self.dfs(node.left, path+[node.left.val], pathsum + node.left.val, sum)
        if node.right:
            self.dfs(node.right, path+[node.right.val], pathsum+node.right.val, sum)


##############


















        #
