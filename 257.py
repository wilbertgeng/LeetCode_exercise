"""257. Binary Tree Paths"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        ### Practice
        if not root:
            return []
        self.res = []
        self.dfs(root, str(root.val))
        return self.res

    def dfs(self, node, path):
        if not node.left and not node.right:
            self.res.append(path)
            return
        if node.left:
            self.dfs(node.left, path+"->"+str(node.left.val))
        if node.right:
            self.dfs(node.right, path+"->"+str(node.right.val))


        ############
        if not root:
            return []
        res = []
        self.dfs_backtrack(root, "", res)
        return res

    def dfs_backtrack(self, node, path, res):
        if not node:
            return None
        if not node.left and not node.right:
            res.append(path + str(node.val))
        self.dfs_backtrack(node.left, path + str(node.val) + "->", res)
        self.dfs_backtrack(node.right, path + str(node.val) + "->", res)


         # dfs + stack
    def binaryTreePaths1(self, root):
        if not root:
            return []
        res, stack = [], [(root, "")]
        while stack:
            node, ls = stack.pop()
            if not node.left and not node.right:
                res.append(ls+str(node.val))
            if node.right:
                stack.append((node.right, ls+str(node.val)+"->"))
            if node.left:
                stack.append((node.left, ls+str(node.val)+"->"))
        return res

    # bfs + queue
    def binaryTreePaths2(self, root):
        if not root:
            return []
        res, queue = [], collections.deque([(root, "")])
        while queue:
            node, ls = queue.popleft()
            if not node.left and not node.right:
                res.append(ls+str(node.val))
            if node.left:
                queue.append((node.left, ls+str(node.val)+"->"))
            if node.right:
                queue.append((node.right, ls+str(node.val)+"->"))
        return res
