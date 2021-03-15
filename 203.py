"""203. Remove Linked List Elements"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        p = dummy = ListNode(0)
        p.next = head
        while p.next:
            if p.next.val == val:
                p.next = p.next.next
            else:
                p = p.next 
        return dummy.next
