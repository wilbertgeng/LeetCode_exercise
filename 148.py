"""148. Sort List"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        pre = None
        slow = head
        fast = head
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next

        pre.next = None

        return self.Merge(self.sortList(head), self.sortList(slow))

    def Merge(self, h1, h2):
        dummy = tail = ListNode(None)
        while h1 and h2:
            if h1.val < h2.val:
                tail.next, h1, tail = h1, h1.next, h1
            else:
                tail.next, h2, tail = h2, h2.next, h2

        tail.next = h1 or h2

        return dummy.next
