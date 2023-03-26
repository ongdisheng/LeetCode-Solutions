# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Time: O(n)
        Space: O(1)
        """

        # create a dummy node
        dummy = ListNode()

        # initialize tail
        tail = dummy

        # loop until either of the lists reaches the end
        while list1 is not None and list2 is not None:

            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            
            else:
                tail.next = list2
                list2 = list2.next
            
            tail = tail.next

        # merge remaining list
        if list1 is not None:
            tail.next = list1
        elif list2 is not None:
            tail.next = list2

        return dummy.next