class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        """
        Time: O(E + V)
        Space: O(E + V)
        """
        # write your code here
        # edge case
        if not n:
            return True
        
        # create adjacency list
        adj = { i: [] for i in range(n) }
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        visit = set()
        def dfs(cur, prev):
            # detect a loop
            if cur in visit:
                return False
            
            visit.add(cur)
            for neigh in adj[cur]:
                # avoid going back to previous node
                if neigh == prev:
                    continue
                
                # detect any loop
                if not dfs(neigh, cur):
                    return False
            
            return True
        
        # no loop and connected
        return dfs(0, -1) and len(visit) == n

                