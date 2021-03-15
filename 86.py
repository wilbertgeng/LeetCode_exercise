"""86. Partition List"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        ##
        prev = prevHead = ListNode(0)
        after = afterHead = ListNode(0)
        while head:
            if head.val < x:
                prev.next = head
                prev = prev.next
            else:
                after.next = head
                after = after.next
            head = head.next
        after.next = None ## !! don't forget this, otherwise cycle happens
        prev.next = afterHead.next
        return prevHead.next


        ###
        prev = dummy = ListNode(0)
        stack = []
        while head:
            if head.val < x:
                prev.next = head
                prev = prev.next
            else:
                stack.append(head.val)
            head = head.next

        while stack:
            nodeVal = stack.pop(0)
            prev.next = ListNode(nodeVal)
            prev = prev.next

        return dummy.next
