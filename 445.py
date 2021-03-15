"""445. Add Two Numbers II"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        """use stack, add ints, then use ListNode(-1) node.val = -1 defaault
         reversely rebuild linkedlist"""
        # Practice:
        stack1 = []
        stack2 = []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next

        head = ListNode(-1)
        c = 0
        while stack1 or stack2:
            if not stack1:
                val = stack2.pop()
            elif not stack2:
                val = stack1.pop()
            else:
                val = stack1.pop() + stack2.pop()
            c, val = divmod(val + c, 10)
            head.val = val
            temp = head
            head = ListNode(-1)
            head.next = temp
        
        if c:
            head.val = c
        
        return head if head.val != -1 else head.next 
        




        #use stack
        stack1 = []
        stack2 = []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next

        while l2:
            stack2.append(l2.val)
            l2 = l2.next

        carry = 0
        head = ListNode(-1)
        while stack1 or stack2:
            if not stack1:
                val = stack2.pop()
            elif not stack2:
                val = stack1.pop()
            else:
                val = stack1.pop() + stack2.pop()
            carry, val = divmod(val + carry, 10)

            head.val = val
            temp = head
            head = ListNode(-1)

            head.next = temp

        if carry: head.val = carry

        return head if head.val != -1 else head.next
