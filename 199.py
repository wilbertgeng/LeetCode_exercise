"""199. Binary Tree Right Side View"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ##### Practice: BFS
        if not root:
            return []

        res = []
        queue = collections.deque()
        res.append(root.val)
        queue = [root]
        tmp = []
        while queue:
            node = queue.pop(0)
            if node.left:
                tmp.append(node.left)
            if node.right:
                tmp.append(node.right)
            if not queue and tmp:
                res.append(tmp[-1].val)
                queue = tmp
                tmp = []
        return res
        ###### Practice: DFS len(res) should equal to tree depth
        def dfs(node, depth):
            if not node:
                return
            if len(res) == depth:
                res.append(node.val)
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)
            
        res = []
        dfs(root, 0)

        return res

    ########
        def collect(node, depth):
            if node:
                if depth == len(view):
                    view.append(node.val)

                collect(node.right, depth + 1)
                collect(node.left, depth + 1)


        view = []
        collect(root, 0)

        return view
