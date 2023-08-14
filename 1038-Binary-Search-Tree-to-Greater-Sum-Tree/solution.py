# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        """
        Time: O(n)
        Space: O(n)
        """
        total = [0]

        def aux(node):
            # base case
            if not node:
                return

            # recursive case
            aux(node.right)
            node.val += total[0]
            total[0] = node.val
            aux(node.left)
        
        aux(root)
        return root