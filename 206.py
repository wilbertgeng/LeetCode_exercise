
"""Reverse a singly linked list."""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        """Note: start with prev = None curr points at prev.
        Curr move to the next and that relation can be passed on. Return from prev"""
        ## Practice
        prev = None
        while head:
            cur = head
            head = head.next
            cur.next = prev
            prev = cur
        return prev
        ### Recursion
        def rev(node):
            if not node or not node.next: ## !! don't miss not
                return node
            newNode = rev(node.next)
            node.next.next = node
            node.next = None
            return newNode
        return rev(head)

        # R1,2
        prev = None

        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr

        return prev
        # Recursion:

        def reverse(head):
            if not head or not head.next:
                return head
            reverseHead = reverse(head.next)
            head.next.next = head
            head.next = None
            return reverseHead
        return reverse(head)









def reverseList(self, head):

    prev = None
    while head:
        curr = head
        head = head.next
        curr.next = prev
        prev = curr
    return prev
