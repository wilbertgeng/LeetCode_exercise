"""133. Clone Graph"""
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        """ My NOTES: 1. Use dict to store nodes. Record visited nodes
          2. Use DFS to visit every neighbor of node,
          copy every node and its neighbors """
        if not node:
            return node
        m = {node:Node(node.val)}
        self.dfs(node, m)
        return m[node]

    def dfs(self, node, m):
        if not node.neighbors:
            return
        for nb in node.neighbors:
            if nb not in m:
                m[nb] = Node(nb.val)
                self.dfs(nb, m)
            m[node].neighbors.append(m[nb])













#######
