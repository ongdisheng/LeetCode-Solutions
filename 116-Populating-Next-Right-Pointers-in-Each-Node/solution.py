"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        """
        Time: O(n)
        Space: O(1)
        """
        # initialize variables
        node = root

        # base case
        if node is None or node.left is None:
            return node
        
        # recursive case
        node.left.next = node.right
        if node.next is not None:
            node.right.next = node.next.left

        self.connect(node.left)
        self.connect(node.right)
        return node