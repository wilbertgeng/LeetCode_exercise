"""Merge Two Sorted Lists

Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        #### Practice:
        n = dummy = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                n.next = l1
                l1 = l1.next
            else:
                n.next = l2
                l2 = l2.next
            n = n.next
        n.next = l1 or l2
        return dummy.next


        ######R2: please refer to 23.py
        dummy = head = ListNode(0) #initialize a dummy head at ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                dummy.next = l1
                l1 = l1.next
            else:
                dummy.next = l2
                l2 = l2.next

            dummy = dummy.next

        dummy.next = l1 or l2

        return head.next

####################R1:

        ptr = head = ListNode(0)

        while True:

            if not l1 or not l2:
                ptr.next = l1 or l2
                break
            else:
                smallVal = 0
                if l1.val < l2.val:
                    smallVal = l1.val
                    l1 = l1.next
                else:
                    smallVal = l2.val
                    l2 = l2.next

                NewNode = ListNode(smallVal)
                ptr.next = NewNode
                ptr = ptr.next
        return head.next
""" Recursive solution """
#solution 2
def mergeTwoLists(self, a, b):
    if a and b:
        if a.val > b.val:
            a, b = b, a
        a.next = self.mergeTwoLists(a.next, b)
    return a or b

#solution3
def mergeTwoLists(self, a, b):
    if not a or b and a.val > b.val:
        a, b = b, a
    if a:
        a.next = self.mergeTwoLists(a.next, b)
    return a
