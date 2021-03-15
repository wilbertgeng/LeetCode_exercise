"""116. Populating Next Right Pointers in Each Node"""
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        ### BFS
        if not root:
            return None
        queue = collections.deque()
        queue.append(root)
        while queue:
            curr = queue.popleft()
            if curr.left and curr.right:
                curr.left.next = curr.right
                queue.append(curr.left)
                queue.append(curr.right)
                if curr.next:
                    curr.right.next = curr.next.left
        return root

        
        ### dfs
        if not root:
            return None

        self.connect2Nodes(root.left, root.right)
        return root

    def connect2Nodes(self, node1, node2):
        if not node1 or not node2:
            return

        node1.next = node2
        self.connect2Nodes(node1.left, node1.right)
        self.connect2Nodes(node1.right, node2.left)
        self.connect2Nodes(node2.left, node2.right)
