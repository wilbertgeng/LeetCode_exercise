"""430. Flatten a Multilevel Doubly Linked List"""
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None
        stack = [head]
        dummy = prev = Node(0)
        while stack:
            node = stack.pop()
            node.prev = prev
            prev.next = node
            if node.next:
                stack.append(node.next)
                node.next = None  ## !! don't forget to cut off
            if node.child:
                stack.append(node.child)
                node.child = None   ## !! cut off child
            prev = node
        dummy.next.prev = None
        return dummy.next
