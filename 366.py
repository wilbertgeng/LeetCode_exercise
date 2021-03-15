"""366. Find Leaves of Binary Tree"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        d = collections.defaultdict(list)
        self.dfs(root, d)
        for i in d:
            res.append(d[i])
        return res

    def dfs(self, node, d):
        if not node:
            return 0
        level = max(self.dfs(node.left, d), self.dfs(node.right, d))+1
        d[level].append(node.val)
        return level 
