"""725. Split Linked List in Parts"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        # Practice：
        curr = root
        ct = 0
        while curr:
            ct += 1
            curr = curr.next
        
        bucket_size = ct/k
        longer_bucket = ct%k
        res = [bucket_size + 1]*longer_bucket + [bucket_size]*(k-longer_bucket)

        prev = None
        curr = root
        for idx, length in enumerate(res):
            res[idx] = curr
            if prev:
                prev.next = None
            for i in range(length):
                prev = curr
                curr = curr.next

        return res


        # R：
        length = 0
        curr = root
        ## find the length of linkedlist
        while curr:
            length += 1
            curr = curr.next
        ## find bucketsize and number of longer buckets
        bucket_size, longer_bucket = length//k, length%k
        ## build res with buckets
        res = [bucket_size + 1]*longer_bucket + [bucket_size]*(k - longer_bucket)

        prev = None #### to cut the linkedlist
        curr = root
        for index, num in enumerate(res): ##num is bucket size
            res[index] = curr
            if prev:
                prev.next = None ## to cut the linkedlist from prev bucket
            for i in range(num):
                prev, curr = curr, curr.next

        return res
