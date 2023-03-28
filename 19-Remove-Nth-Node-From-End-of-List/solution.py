# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Time: O(n)
        Space: O(1)
        """

        # create dummy node
        dummy = ListNode(next = head)

        # initialize left and right pointer
        left = dummy
        right = head

        # move right pointer
        while n > 0 and right is not None:
            right = right.next
            n -= 1
        
        # move left and right pointer
        while right is not None:
            right = right.next
            left = left.next
        
        # delete
        left.next = left.next.next
        return dummy.next