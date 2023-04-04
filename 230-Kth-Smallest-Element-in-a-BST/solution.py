# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        Idea: Iterative
        Time: O(n)
        Space: O(n)
        """

        # initialize number of processed nodes, stack and current node
        n = 0
        stack = []
        cur = root

        # in order traversal
        while cur is not None or len(stack) > 0:

            # traverse left subtree
            while cur is not None:
                stack.append(cur)
                cur = cur.left
            
            # pop from stack
            cur = stack.pop()

            # update number of processed node
            n += 1

            if n == k:
                return cur.val
            
            # traverse right subtree
            cur = cur.right