"""95. Unique Binary Search Trees II"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        ### review practice:
        if n == 0:
            return []
        return self.dfs(1, n+1)

    def dfs(self, start, end):
        if start == end:
            return None
        result = []
        for i in range(start, end):
            for l in self.dfs(start, i) or [None]:
                for r in self.dfs(i+1, end) or [None]:
                    node = TreeNode(i)
                    node.left = l
                    node.right = r
                    result.append(node)
        return result 






        #### R1:
        if n == 0:
            return []

        return self.dfs(1, n + 1)

    def dfs(self, start, end):
        if start == end:
            return None
        result = []
        for i in range(start, end):
            for l in self.dfs(start, i) or [None]:
                for r in self.dfs(i + 1, end) or [None]:
                    node = TreeNode(i)
                    node.left = l
                    node.right = r
                    result.append(node)

        return result
