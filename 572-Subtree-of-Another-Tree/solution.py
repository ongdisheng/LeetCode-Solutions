# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        Time: O(s * t)
        Space: O(s + t)
        """

        # base case
        if subRoot is None:
            return True
        if root is None:
            return False
        if self.sameTree(root, subRoot):
            return True

        # recursive case
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def sameTree(self, root, subRoot):
        # base case
        if root is None and subRoot is None:
            return True
        if root is not None and subRoot is not None and root.val == subRoot.val:
            return self.sameTree(root.left, subRoot.left) and self.sameTree(root.right, subRoot.right)
        return False