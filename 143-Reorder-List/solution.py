# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        Time: O(n)
        Space: O(1)
        """

        # find middle point separating two halves
        slow, fast = head, head.next
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        
        # reverse second halve
        second = slow.next
        prev = slow.next = None
        while second is not None:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        # merge two halves
        first, second = head, prev
        while second is not None:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2
