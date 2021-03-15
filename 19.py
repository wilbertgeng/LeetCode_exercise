"""Remove Nth Node From End of List

Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        """ Note: slow, fast pointer, fast ptr N steps ahead """
############ Practice:
        fast = slow = head
        for i in range(n):
            fast = fast.next

        if not fast:
            return head.next
        
        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return head
####### R2:
        
        # find K
        numNode = 0
        tmp = head
        while tmp is not None:
            tmp = tmp.next
            numNode +=1
            k = numNode - n

        prev = None
        ptr = head
        while k != 0:
            prev = ptr
            ptr = ptr.next
            k -= 1

        if prev == None:
            return head.next
        else:
            prev.next = ptr.next
            ptr.next = None

        return head

    #solution 2: n ahead
class Solution2(object):
    def removeNthFromEnd2(self, head, n):
        fast = slow = head

        for i in range(n):
            fast = fast.next

        if fast is None:
            return head.next
        else:
            while fast.next:
                slow = slow.next
                fast = fast.next

            slow.next = slow.next.next

            return head
