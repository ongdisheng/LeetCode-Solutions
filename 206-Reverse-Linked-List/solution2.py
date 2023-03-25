# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Time: O(n)
        Space: O(n)
        """

        # base case
        if head is None:
            return None
        
        # recursive case
        new_head = head
        if head.next is not None:

            # recurse to smaller list
            new_head = self.reverseList(head.next)

            # reverse link
            head.next.next = head
        
        # ensure end of reversed linked list points to None
        head.next = None

        # new_head: end of original linked list
        return new_head
        