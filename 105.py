"""105. Construct Binary Tree from Preorder and Inorder Traversal"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        ## Practice:
        map = {}
        for i in range(len(inorder)):
            map[inorder[i]] = i
        self.nodes = iter(preorder)
        return self.dfs(map, 0, len(preorder)-1)

    def dfs(self, map, start, end):
        if start > end:
            return None
        nodeVal = self.nodes.next()
        node = TreeNode(nodeVal)
        node.left = self.dfs(map, start, map[nodeVal]-1)
        node.right = self.dfs(map, map[nodeVal]+1, end)

        return node 



        #### Practice 1/31
        inMap = {}
        n = len(preorder)
        for i in range(n):
            inMap[inorder[i]] = i

        self.nodeVals = iter(preorder)
        return self.dfs(0, n - 1, inMap)

    def dfs(self, start, end, inMap):
        if start > end:
            return None
        nodeVal = self.nodeVals.next()
        node = TreeNode(nodeVal)
        node.left = self.dfs(start, inMap[nodeVal] - 1, inMap)
        node.right = self.dfs(inMap[nodeVal] + 1, end, inMap)

        return node





        ### Practice
        inMap = {}
        for i in range(len(inorder)):
            inMap[inorder[i]] = i
        self.cnt = 0
        return self.dfs(0, len(preorder)-1, inMap, preorder)

    def dfs(self, start, end, inMap, preorder):
        if start > end:
            return None
        node_val = preorder[self.cnt]
        node = TreeNode(node_val)
        self.cnt += 1
        idx = inMap[node_val]
        node.left = self.dfs(start, idx - 1, inMap, preorder)
        node.right = self.dfs(idx + 1, end, inMap, preorder)

        return node



        #### Essantially a pre order:
        inMap = {}
        for i, num in enumerate(inorder):
            inMap[num] = i
        # pre_iter = iter(preorder), node_val = next(pre_iter)
        # reduce 1 object instance
        self.cnt = 0
        return self.dfs(0, len(preorder)-1, inMap, preorder)

    def dfs(self, start, end, inMap, preorder):
        if start > end:
            return None
        node_val = preorder[self.cnt]
        node = TreeNode(node_val)
        self.cnt += 1
        idx = inMap[node_val]
        node.left = self.dfs(start, idx - 1, inMap, preorder)
        node.right = self.dfs(idx + 1, end, inMap, preorder)
        return node

        ####
        n_dict = {}
        pre_iter = iter(preorder) # iter() function returns an iterator for the given object
        for i, num in enumerate(inorder):
            n_dict[num] = i

        def helper(start, end):
            if start > end: return None
            root_val = next(pre_iter)
            root = TreeNode(root_val)
            idx = n_dict[root_val]

            root.left = helper(start, idx-1)
            root.right = helper(idx+1, end)
            return root

        return helper(0, len(preorder)-1)
