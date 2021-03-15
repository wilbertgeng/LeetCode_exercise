"""83. Remove Duplicates from Sorted List"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # practice:
        # R1,2
        dummy = head

        while head:
            while head.next and head.val == head.next.val:
                head.next = head.next.next

            head = head.next
        return dummy


###############



        cur = head
        while cur:
            while cur.next and cur.next.val == cur.val:
                cur.next = cur.next.next     # skip duplicated node
            cur = cur.next     # not duplicate of current node, move to next node
        return head
