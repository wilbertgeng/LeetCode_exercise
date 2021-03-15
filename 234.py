"""Palindrome Linked List"""

# Definition for singly-linked list.

class Solution(object):
""" reverse the linkedlist see if they are same. use list to compare """
    def isPalindrome(self, head):
        #### Practice
        val = []
        while head:
            val.append(head.val)
            head = head.next
        return val == val[::-1]
        ## Two Pointers
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        prev = None
        while slow:
            cur = slow
            slow = slow.next
            cur.next = prev
            prev = cur

        while prev:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
        return True






        ####
        val = []
        while head:
            val.append(head.val)
            head = head.next
        return True if val == val[::-1] else False




class Solution(object):
    def isPalindrome(self, head):
        vals = []
        while head:
            vals += head.val
            head = head.next

        return val ==val[::-1]

#solution2:
"""fast slow pointers"""
class Solution(object):
    def isPalindrome(self,head):
        prev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        while slow:
            curr = slow
            slow = slow.next # save next(slow)
            curr.next = prev
            prev = curr


        while prev:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
        return True
