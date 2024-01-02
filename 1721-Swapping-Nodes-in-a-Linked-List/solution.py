# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Time: O(n)
        Space: O(1)
        """
        # initialize variables
        pre_left = pre_right = dummy = ListNode(next=head) 
        left = right = head

        # move left
        for _ in range(k-1):
            pre_left = left
            left = left.next
        
        # move right
        temp = left
        while temp.next:
            pre_right = right
            right = right.next
            temp = temp.next
        
        # no need swap
        if left == right:
            return head
        
        pre_left.next, pre_right.next = right, left
        left.next, right.next = right.next, left.next 
        return dummy.next