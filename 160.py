# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        """Note: two dummy head on each end, set two counter to count cycle time """
        if headA == None or headB == None:
            return None

        p_A = headA
        p_B = headB
        count1 = 0
        count2 = 0

        while True:
            if p_A == p_B:
                return p_A

            if p_A != None:
                p_A = p_A.next

            else:
                p_A = headB
                count1 += 1

            if p_B != None:
                p_B = p_B.next

            else:
                p_B = headA
                count2 += 1

            if count1 == 2 or count2 == 2:
                return None











#############
        if headA == None or headB == None:
            return None

        p_A = headA
        p_B = headB

        swapA= 0
        swapB = 0
        while True:
            if p_A == p_B:
                return p_A

            if p_A != None:
                p_A = p_A.next
            else:
                p_A = headB
                swapA += 1


            if p_B != None:
                p_B = p_B.next
            else:
                p_B = headA
                swapB += 1

            if swap_A == 2 or swap_B == 2:
                return None
