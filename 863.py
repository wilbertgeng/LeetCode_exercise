"""863. All Nodes Distance K in Binary Tree"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        graph = collections.defaultdict(list)
        visited = set()
        # to record adjacent nodes, build Graph
        def dfs(node):
            if node.left:
                graph[node].append(node.left)
                graph[node.left].append(node)
                dfs(node.left)
            if node.right:
                graph[node].append(node.right)
                graph[node.right].append(node)
                dfs(node.right)

        dfs(root)
        res = []
        def search(node, depth):
            visited.add(node)
            if depth < K:
                for k in graph[node]:
                    if k not in visited:
                        search(k, depth+1)
            else:
                res.append(node.val)

        search(target, 0)
        return res
















#####
