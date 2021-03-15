"""142. Linked List Cycle II"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = fast = head
        while fast and fast.next: #has to be fast not slow 
            slow = slow.next
            fast = fast.next.next
            if slow == fast:

                slow1 = head
                while slow1 != slow:
                    slow = slow.next
                    slow1 = slow1.next

                return slow
