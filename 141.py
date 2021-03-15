
"""Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list,
we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to.
If pos is -1, then there is no cycle in the linked list.

Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node.


Example 2:

Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the first node.
"""
class Solution(object):
    def hasCycle(self, head):

        ## R2 Solution2:
slow = fast = head
    while fast and fast.next: ## while loop has to be written like this
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            return True
    return False


## R1 (fast)
        try:
            slow = head
            fast = head.next

            while slow != fast:
                slow = slow.next
                fast = fast.next.next

            return True
        except:
            return False
