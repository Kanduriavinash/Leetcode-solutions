from collections import deque

class Solution(object):
    def findMaxPathScore(self, edges, online, k):
        """
        :type edges: List[List[int]]
        :type online: List[bool]
        :type k: int
        :rtype: int
        """
        n = len(online)

        graph = [[] for _ in range(n)]
        indeg = [0] * n
        costs = []

        for u, v, w in edges:
            graph[u].append((v, w))
            indeg[v] += 1
            costs.append(w)

        # Topological Sort
        q = deque()
        for i in range(n):
            if indeg[i] == 0:
                q.append(i)

        topo = []
        while q:
            u = q.popleft()
            topo.append(u)
            for v, _ in graph[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)

        INF = float('inf')

        def can(score):
            dist = [INF] * n
            dist[0] = 0

            for u in topo:
                if dist[u] == INF:
                    continue

                # Intermediate node must be online
                if u != 0 and u != n - 1 and not online[u]:
                    continue

                for v, w in graph[u]:
                    if w < score:
                        continue
                    if v != n - 1 and not online[v]:
                        continue
                    if dist[u] + w < dist[v]:
                        dist[v] = dist[u] + w

            return dist[n - 1] <= k

        if not costs:
            return -1

        costs = sorted(set(costs))

        if not can(costs[0]):
            return -1

        lo, hi = 0, len(costs) - 1
        ans = costs[0]

        while lo <= hi:
            mid = (lo + hi) // 2
            if can(costs[mid]):
                ans = costs[mid]
                lo = mid + 1
            else:
                hi = mid - 1

        return ans