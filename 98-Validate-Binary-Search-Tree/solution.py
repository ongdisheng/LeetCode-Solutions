# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        Time: O(n)
        Space: O(n)
        """

        # inner function
        def valid(node, left, right):

            # base case
            if node is None:
                return True
            
            if not (left < node.val < right):
                return False
            
            # recursive case
            return valid(node.left, left, node.val) and valid(node.right, node.val, right)
        
        return valid(root, float("-inf"), float("inf"))