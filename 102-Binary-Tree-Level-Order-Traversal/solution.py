# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Time: O(n)
        Space: O(n)
        """

        # initialize res and queue
        res = []
        queue = collections.deque()
        queue.append(root)

        # BFS
        while len(queue) > 0:

            # initialize level list and number of nodes in current level
            level = []
            num_of_nodes_in_cur_level = len(queue)

            # iterate over every node in current level
            for i in range(num_of_nodes_in_cur_level):

                # pop from queue
                node = queue.popleft()
                
                # append node val to level
                # append its child to queue
                if node is not None:
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            
            # append level list to res
            if len(level) > 0:
                res.append(level)
        
        return res