class Solution(object):
    def countCompleteComponents(self, n, edges):
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n
        ans = 0

        def dfs(node, comp):
            visited[node] = True
            comp.append(node)
            for nei in graph[node]:
                if not visited[nei]:
                    dfs(nei, comp)

        for i in range(n):
            if not visited[i]:
                comp = []
                dfs(i, comp)

                size = len(comp)
                complete = True

                for node in comp:
                    if len(graph[node]) != size - 1:
                        complete = False
                        break

                if complete:
                    ans += 1

        return ans