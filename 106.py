"""106. Construct Binary Tree from Inorder and Postorder Traversal"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        ## Practice:
        map = {}
        for i in range(len(inorder)):
            map[inorder[i]] = i
        self.cnt = len(postorder)-1
        self.postorder = postorder
        return self.dfs(map, 0, len(postorder)-1)

    def dfs(self, map, start, end):
        if start > end:
            return None
        nodeVal = self.postorder[self.cnt] ## reversed order when pop postorder eles
        self.cnt -= 1
        node = TreeNode(nodeVal)
        node.right = self.dfs(map, map[nodeVal]+1, end) ## !! start, end diff than 105
        node.left = self.dfs(map, start, map[nodeVal]-1)

        return node





        ######
        inMap = {}
        for i, num in enumerate(inorder):
            inMap[num] = i
        self.cnt = len(postorder) - 1

        return self.dfs(0, len(postorder)-1, postorder,inMap)

    def dfs(self, start, end, postorder, inMap):
        if start > end:
            return None
        node_val = postorder[self.cnt]
        node = TreeNode(node_val)
        idx = inMap[node_val]
        self.cnt -= 1
        node.right = self.dfs(idx+1, end, postorder, inMap)
        node.left = self.dfs(start, idx-1, postorder, inMap)

        return node
