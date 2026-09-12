class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        a = []
        for i in range(n):
            a.append([intervals[i][0], intervals[i][1], intervals[i][2], i])
        a.sort()
        ls = [a[i][0] for i in range(n)]

        s = [[0]*5 for _ in range(n+1)]
        p = [[[] for _ in range(5)] for _ in range(n+1)]

        for i in range(n-1, -1, -1):
            nx = bisect_right(ls, a[i][1])
            for k in range(5):
                s[i][k] = s[i+1][k]
                p[i][k] = p[i+1][k]
            for k in range(1, 5):
                t = a[i][2] + s[nx][k-1]
                q = sorted(p[nx][k-1] + [a[i][3]])
                if t > s[i][k] or (t == s[i][k] and q < p[i][k]):
                    s[i][k] = t
                    p[i][k] = q

        return p[0][4]