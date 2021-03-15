"""92. Reverse Linked List II"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        ### Practice:
        if m == n or not head:
            return head
        p = dummy = ListNode(0)
        p.next = head
        for i in range(m-1):
            p = p.next
        tail = p.next
        for i in range(n - m):
            tmp = p.next
            p.next = tail.next
            tail.next = tail.next.next
            p.next.next = tmp
        return dummy.next


        ## Practice:
        if m == n or not head:
            return head
        cur = dummy = ListNode(0)
        dummy.next = head
        for i in range(m-1):
            cur = cur.next
        tail = cur.next
        for i in range(n - m):
            tmp = p.next
            p.next = tail.next
            tail.next = tail.next.next
            p.next.next = tmp
        return dummy.next

        ##
        if m == n or not head:
            return head
        dummy = ListNode(0)
        dummy.next = head
        p = dummy
        for i in range(m-1):
            p = p.next
        tail = p.next
        for j in range(n-m):
            tmp = p.next
            p.next = tail.next
            tail.next = tail.next.next
            p.next.next = tmp
        return dummy.next
