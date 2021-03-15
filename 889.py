"""889. Construct Binary Tree from Preorder and Postorder Traversal"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """
        self.indexPre = 0
        self.indexPost = 0
        return self.dfs(pre, post)

    def dfs(self, pre, post):
        nodeVal = pre[self.indexPre]
        node = TreeNode(nodeVal)
        self.indexPre += 1
        if nodeVal != post[self.indexPost]:
            node.left = self.dfs(pre, post)
        if nodeVal != post[self.indexPost]:
            node.right = self.dfs(pre, post)
        self.indexPost += 1

        return node
