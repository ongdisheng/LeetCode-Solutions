# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Time: O(n)
        Space: O(1)
        """
        # initialize prev and current pointer
        prev, current = None, head

        # loop until the end of linked list
        while current is not None:

            # temp pointer
            nxt = current.next

            # reverse 
            current.next = prev

            # update prev and current pointer
            prev = current
            current = nxt

        return prev