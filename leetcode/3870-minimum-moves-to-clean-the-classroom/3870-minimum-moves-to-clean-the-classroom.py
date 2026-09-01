from collections import deque

class Solution(object):
    def minMoves(self, classroom, energy):
        m = len(classroom)
        n = len(classroom[0])

        litter = {}
        sr = sc = 0
        k = 0

        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    sr, sc = r, c
                elif classroom[r][c] == 'L':
                    litter[(r, c)] = k
                    k += 1

        if k == 0:
            return 0

        full = (1 << k) - 1

        best = [
            [[-1] * (1 << k) for _ in range(n)]
            for _ in range(m)
        ]

        q = deque([(sr, sc, energy, 0, 0)])
        best[sr][sc][0] = energy

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while q:
            r, c, e, mask, moves = q.popleft()

            if mask == full:
                return moves

            if e == 0:
                continue

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if not (0 <= nr < m and 0 <= nc < n):
                    continue

                if classroom[nr][nc] == 'X':
                    continue

                ne = e - 1
                nmask = mask

                if classroom[nr][nc] == 'L':
                    nmask |= 1 << litter[(nr, nc)]

                if classroom[nr][nc] == 'R':
                    ne = energy

                if best[nr][nc][nmask] >= ne:
                    continue

                best[nr][nc][nmask] = ne
                q.append((nr, nc, ne, nmask, moves + 1))

        return -1