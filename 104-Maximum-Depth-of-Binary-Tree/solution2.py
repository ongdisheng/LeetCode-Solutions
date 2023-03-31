# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        Idea: Iterative BFS 
        Time: O(n)
        Space: O(n)
        """

        # base case
        if root is None:
            return 0
        
        # initialize queue and level
        queue = deque([root])
        level = 0

        # BFS
        while queue:

            # iterate over nodes by level
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            
            level += 1
        
        return level