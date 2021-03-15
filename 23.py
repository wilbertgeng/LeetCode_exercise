"""23. Merge k Sorted Lists"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None

        if len(lists) == 1:
            return lists[0]

        mid = len(lists)//2
        l, r = self.mergeKLists(lists[:mid]), self.mergeKLists(lists[mid:])
        return self.merge(l, r)

    def merge(self, l, r):
        dummy = start = ListNode(0)
        while l and r:
            if l.val <= r.val:
                start.next = l
                l = l.next

            else:
                start.next = r 
                r = r.next
            start = start.next
        start.next = l or r

        return dummy.next
