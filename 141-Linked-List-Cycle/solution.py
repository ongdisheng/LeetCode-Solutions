# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Idea: Floyd's Tortoise and Hare
        Time: O(n)
        Space: O(1)
        """

        # initialize slow and fast pointer
        slow, fast = head, head

        # not yet reach the end of linked list (null)
        while fast is not None and fast.next is not None:

            # update slow and fast
            slow = slow.next
            fast = fast.next.next

            # fast meetup slow 
            if fast == slow:
                return True
        
        return False