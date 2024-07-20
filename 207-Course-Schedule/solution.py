class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Time: O(V + E)
        Space: O(V + E)
        """
        # initialize prerequisites map
        pre_map = { i: [] for i in range(numCourses) }
        visit = set()

        # update map
        for course, preq in prerequisites:
            pre_map[course].append(preq)

        def dfs(node):
            # base case
            # encounter a loop
            if node in visit:
                return False
            
            if pre_map[node] == []:
                return True
            
            visit.add(node)
            for preq in pre_map[node]:
                if not dfs(preq):
                    return False
            
            # remove node from visit
            visit.remove(node)
            pre_map[node] = []
            return True

        # use loop to avoid disconnected graph
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True