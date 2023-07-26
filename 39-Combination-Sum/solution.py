class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Time: O(2 ^ t)
        Space: O(t) due to recursive stack
        """
        # initialize res variable
        res = []

        def dfs(i, cur, total): 
            # base case
            if total == target:
                res.append(cur.copy())
                return

            if i >= len(candidates) or total > target:
                return

            # recursive case
            # include
            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])

            # exclude
            cur.pop()
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res
