# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Time: O(p + q)
        Space: O(p + q)
        """

        # base case
        # both p and q are empty
        if p is None and q is None:
            return True
        
        # either of p and q is empty
        if p is None or q is None:
            return False
        
        # p and q having different value
        if p.val != q.val:
            return False
        
        # recursive case
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)