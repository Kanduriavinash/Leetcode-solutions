class Solution(object):
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        """
        :type n: int
        :type nums: List[int]
        :type maxDiff: int
        :type queries: List[List[int]]
        :rtype: List[bool]
        """

        parent = [i for i in range(n)]

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            pa = find(a)
            pb = find(b)

            if pa != pb:
                parent[pb] = pa

        for i in range(n - 1):
            if nums[i + 1] - nums[i] <= maxDiff:
                union(i, i + 1)

        ans = []

        for u, v in queries:
            if find(u) == find(v):
                ans.append(True)
            else:
                ans.append(False)

        return ans