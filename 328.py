"""328. Odd Even Linked List"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy1 = odd = ListNode(0)
        dummy2 = even = ListNode(0)
    
        while head:
            odd.next = head
            even.next = head.next

            odd = odd.next
            even = even.next
            ### head jump two steps
            head = head.next.next if even else None
        odd.next = dummy2.next

        return dummy1.next
