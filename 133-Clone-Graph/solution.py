"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        """
        Time: O(V + E)
        Space: O(V)
        """
        # initialize map (old to new)
        map = {}

        def dfs(node):
            # base case
            if node in map:
                return map[node]
            
            # create clone
            clone = Node(val=node.val)
            map[node] = clone

            # append clone neighbours
            for neigh in node.neighbors:
                clone.neighbors.append(dfs(neigh))

            return clone
        
        return dfs(node) if node else None