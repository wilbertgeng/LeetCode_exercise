"""Maximum Depth of Binary Tree

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.

"""

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ##### Practice:
        ### DFS:
        if not root:
            return 0
        depth = 0
        return self.dfs(root, depth)
    def dfs(self, node, depth):
        if not node:
            return depth
        return max(self.dfs(node.left, depth+1), self.dfs(node.right, depth+1))

        ##### BFS
        if not root:
            return 0
        queue = [root]
        tmp = []
        cnt = 0
        while queue:
            node = queue.pop(0)
            if node.left:
                tmp.append(node.left)
            if node.right:
                tmp.append(node.right)
            if not queue:
                queue = tmp
                tmp = []
                cnt += 1
        return cnt









        ###  R2:
        if root == None:
            return 0
        ### number of returns is number of depth
        return max(self.maxDepth(root.left)+1, self.maxDepth(root.right)+1)





        if not root:
            return 0

        return 1+ max(self.maxDepth(root.left), self.maxDepth(root.right))
