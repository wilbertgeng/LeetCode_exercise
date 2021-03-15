"""143. Reorder List"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head:
            return None
        dummy = ListNode(0)
        dummy.next = slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        dummy2 = ListNode(0)
        dummy2.next = slow

        prev = None
        while slow:
            curr = slow
            slow = slow.next
            curr.next = prev
            prev = curr
        p = dummy.next
        q = prev
        n = newHead = ListNode(0)
        while p and q:
            n.next = p
            p = p.next
            n = n.next
            n.next = q
            q = q.next
            n = n.next

        n.next = None
        return newHead.next
