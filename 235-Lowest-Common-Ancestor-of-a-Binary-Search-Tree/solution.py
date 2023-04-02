# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Time: O(log n)
        Space: O(1)
        """

        # initialize current to be the root node
        cur = root

        # search for LCA
        while cur is not None:

            # no split
            # search left subtree
            if p.val < cur.val and q.val < cur.val:
                cur = cur.left
            
            # no split
            # search right subtree
            elif p.val > cur.val and q.val > cur.val:
                cur = cur.right
            
            # split exists
            # either p or q has the same value as current node
            else:
                return cur
