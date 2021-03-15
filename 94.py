"""Binary Tree Inorder Traversal"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ## Practice:
        res = []
        self.dfs(root, res)
        return res

    def dfs(self, node, res):
        if not node:
            return
        self.dfs(node.left, res)
        res.append(node.val)
        self.dfs(node.right, res)
        # iterative:
        curr = root
        stack = []
        res = []
        while True:
            while curr:
                stack.append(curr)
                curr = curr.left
            if not stack:
                return res
            node = stack.pop()
            res.append(node.val)
            curr = node.right

        return res
        # recursive
        res = []
        self.dfs(root, res)
        return res

    def dfs(self, node, res):
        if node:
            self.dfs(node.left, res)
            res.append(node.val)
            self.dfs(node.right, res)

        # iterative
        res = []
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return res
            root = stack.pop()
            res.append(root.val)
            root = root.right
