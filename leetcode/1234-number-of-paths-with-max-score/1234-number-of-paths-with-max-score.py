class Solution(object):
    def pathsWithMaxScore(self, board):
        MOD = 10**9 + 7
        n = len(board)

        dp = [[[-1, 0] for _ in range(n)] for _ in range(n)]

        dp[n-1][n-1] = [0, 1]

        for i in range(n-1, -1, -1):
            for j in range(n-1, -1, -1):

                if board[i][j] == 'X':
                    continue

                if i == n-1 and j == n-1:
                    continue

                best = -1
                count = 0

                for x, y in [(i+1, j), (i, j+1), (i+1, j+1)]:
                    if x < n and y < n and dp[x][y][0] != -1:

                        score = dp[x][y][0]

                        if score > best:
                            best = score
                            count = dp[x][y][1]

                        elif score == best:
                            count += dp[x][y][1]

                if best != -1:
                    val = 0 if board[i][j] == 'E' else int(board[i][j])

                    dp[i][j][0] = best + val
                    dp[i][j][1] = count % MOD

        if dp[0][0][0] == -1:
            return [0, 0]

        return [dp[0][0][0], dp[0][0][1] % MOD]