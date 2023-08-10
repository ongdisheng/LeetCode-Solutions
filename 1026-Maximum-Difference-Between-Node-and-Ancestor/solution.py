# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        """
        Time: O(n)
        Space: O(n)
        """
        
        def dfs(node, mx, mn):
            # base case
            if node is None:
                return 0
            
            # compute current best difference
            res = max(abs(node.val - mx), abs(node.val-mn))
            mn, mx = min(mn, node.val), max(mx, node.val)
            return max(res, dfs(node.left, mx, mn), dfs(node.right, mx, mn))
        
        return dfs(root, root.val, root.val)