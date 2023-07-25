# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        Time: O(n)
        Space: O(n)
        """
        # initialize result variable 
        res = [root.val]

        # return max path sum without split
        def dfs(node):
            # base case
            if node is None:
                return 0
            
            # recursive case
            left_max = dfs(node.left)
            right_max = dfs(node.right)

            # handle possible negative values
            left_max = max(left_max, 0)
            right_max = max(right_max, 0)

            # update res
            # compute max path sum with split
            res[0] = max(res[0], node.val + left_max + right_max)

            return node.val + max(left_max, right_max)

        dfs(root)
        return res[0]