"""109. Convert Sorted List to Binary Search Tree"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        ### Practice:
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        tmp = slow
        slow = None
        root = TreeNode(tmp.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(tmp.next)

        return root

s = Solution()
ans = s.sortedListToBST()

        ##############
        if not head:
            return

        if not head.next:
            return TreeNode(head.val)

        slow = head
        fast = head.next.next ## one step ahead

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        tmp = slow.next
        slow.next = None
        root = TreeNode(tmp.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(tmp.next)

        return root
