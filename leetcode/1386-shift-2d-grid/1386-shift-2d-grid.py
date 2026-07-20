class Solution(object):
    def shiftGrid(self, grid, k):
        m = len(grid)
        n = len(grid[0])

        arr = []
        for row in grid:
            arr.extend(row)

        total = m * n
        k %= total
        arr = arr[-k:] + arr[:-k]

        res = []
        idx = 0
        for i in range(m):
            res.append(arr[idx:idx + n])
            idx += n

        return res