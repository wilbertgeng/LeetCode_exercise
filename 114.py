"""114. Flatten Binary Tree to Linked List"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        ## Practice:
        self.dfs(root)

    def dfs(self, node):
        if not node:
            return
        self.dfs(node.left)
        self.dfs(node.right)
        left = node.left
        right = node.right

        node.right = left
        node.left = None
        while node.right:
            node = node.right
        node.right = right

        ###
        self.prev = None
        self.dfs(root)
        return root

    def dfs(self, node):
        if not node: #base case
            return

        self.dfs(node.left)
        self.dfs(node.right)
        # 后序遍历位置
        # 1 左右子树已经被拉平成一条链表
        left = node.left
        right = node.right
        # 2 将左子树作为右子树
        node.left = None
        node.right = left
        # 3 将原先的右子树接到当前右子树的末端
        while node.right:
            node = node.right
        node.right = right


        ###
        if not root:
            return None

        self.flatten(root.right)
        self.flatten(root.left)

        root.right = self.prev
        root.left = None
        self.prev = root
