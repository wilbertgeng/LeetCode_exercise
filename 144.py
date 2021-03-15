"""144. Binary Tree Preorder Traversal"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ### BFS
        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            if not node:
                continue
            res.append(node.val)
            stack.append(node.right)
            stack.append(node.left)

        return res
        #### preorder
        res = []
        self.dfs(root, res)
        return res

    def dfs(self, node, res):
        if not node:
            return None
        res.append(node.val)
        self.dfs(node.left, res)
        self.dfs(node.right, res)
##### OOP
        self.res = []
        self.dfs(root)
        return self.res

    def dfs(self, node):
        if not node:
            return
        self.res.append(node.val)
        self.dfs(node.left)
        self.dfs(node.right)
