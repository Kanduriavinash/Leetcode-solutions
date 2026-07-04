class Solution(object):
    def minScore(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """

        graph = [[] for _ in range(n + 1)]

        for a, b, d in roads:
            graph[a].append((b, d))
            graph[b].append((a, d))

        visited = set()
        self.ans = float('inf')

        def dfs(city):
            visited.add(city)

            for nei, dist in graph[city]:
                self.ans = min(self.ans, dist)

                if nei not in visited:
                    dfs(nei)

        dfs(1)

        return self.ans