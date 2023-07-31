# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Time: O(n log n)
        Space: O(n)
        """
        # initialize variables
        res = defaultdict(list)

        def dfs(node, x, y):
            # base case
            if node is None:
                return
            
            # recursive case
            res[y].append((x, node.val))
            dfs(node.left, x+1, y-1)
            dfs(node.right, x+1, y+1)
        
        dfs(root, 0, 0)
        result = []

        # sort by col
        for i in sorted(res.keys()):
            temp = []
            # sort by row
            for j in sorted(res[i]):
                temp.append(j[1])
            result.append(temp)

        return result