class Solution:
    def canCross(self, stones: List[int]) -> bool:
        """
        Time: O(n ^ 2)
        Space: O(n ^ 2)
        """
        # initialize variables
        visit = set()

        def dfs(value, unit):
            # base case
            if value + unit not in stones or (value, unit) in visit:
                return False
            
            if value + unit == stones[-1]:
                return True
            
            visit.add((value, unit))
            return dfs(value+unit, unit-1) or dfs(value+unit, unit) or dfs(value+unit, unit+1)
        
        return dfs(stones[0], 1)