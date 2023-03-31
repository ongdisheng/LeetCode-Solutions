# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        Idea: Iterative DFS 
        Time: O(n)
        Space: O(n)
        """

        # base case
        if root is None:
            return 0
        
        # initialize stack and res
        # stack: [node, depth]
        stack = [[root, 1]]
        res = 1
        
        # DFS (pre-order)
        while stack:
            node, depth = stack.pop()

            # there is a possibility where current node is null
            if node:
                res = max(res, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])

        return res