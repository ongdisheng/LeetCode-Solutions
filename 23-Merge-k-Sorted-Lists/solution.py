# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Time: O(n log k)
        Space: O(n)
        """

        # edge case
        if not lists or len(lists) == 0:
            return None

        # merge k sorted lists
        while len(lists) > 1:
            merged_lists = []

            # merge every two sorted lists
            for i in range(0, len(lists), 2):

                # get the two sorted lists
                list1 = lists[i]
                if i+1 < len(lists):
                    list2 = lists[i+1]
                else:
                    list2 = None

                # merge the two sorted lists
                merged_lists.append(self.mergeTwoLists(list1, list2))
            
            # update lists
            lists = merged_lists
        
        return lists[0]

    def mergeTwoLists(self, list1, list2):
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