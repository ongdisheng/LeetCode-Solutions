class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """
        Time: O(E log N)
        Space: O(n)
        """
        # initialise parent and rank
        parent = [i for i in range(n)]
        rank = [1] * n

        # find parent of given node
        def find(node):
            res = node

            while res != parent[res]:
                # optimize: shorten path to parent node
                parent[res] = parent[parent[res]]
                res = parent[res]
            return res

        def union(n1, n2):
            # find parent nodes
            p1, p2 = find(n1), find(n2)

            # no merge
            if p1 == p2:
                return 0

            # merge
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            
            return 1

        res = n
        for n1, n2 in edges:
            res -= union(n1, n2)
        return res