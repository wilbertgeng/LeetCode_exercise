"""145. Binary Tree Postorder Traversal"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ### bfs
        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            if not node:
                continue
            res.append(node.val)
            stack.append(node.left)
            stack.append(node.right)

        return res[::-1]
        ### dfs
        res = []
        self.dfs(root, res)
        return res

    def dfs(self, node, res):
        if node:
            self.dfs(node.left, res)
            self.dfs(node.right, res)
            res.append(node.val)
