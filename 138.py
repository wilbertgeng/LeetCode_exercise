"""Copy List with Random Pointer"""

class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution(object):
    # @param head, a RandomListNode
# @return a RandomListNode
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        ##Practice:
        if not head:
            return head
        newNode = dummy = Node(-1)
        d = {}
        while head:
            if head in d:
                newNode.next = d[head]
            elif head:
                node = Node(head.val)
                d[head] = node
                newNode.next = node
            if head.random in d:
                newNode.next.random = d[head.random]
            elif head.random:
                node = Node(head.random.val)
                d[head.random] = node
                newNode.next.random = node
            head = head.next
            newNode = newNode.next
        return dummy.next




        #####
        if not head:
            return None
        index = {}
        dummy = newNode = Node(-1, None, None)
        while head:
            if head in index:
                newNode.next = index[head]
            else:
                 node = Node(head.val, None, None)
                 index[head] = node
                 newNode.next = node
            if head.random in index:
                newNode.next.random = index[head.random]
            elif head.random:
                node = Node(head.random.val, None, None)
                index[head.random] = node
                newNode.next.random = node

            newNode = newNode.next
            head = head.next

        return dummy.next
