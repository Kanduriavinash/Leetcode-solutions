class Solution(object):
    def subsequencePairCount(self, nums):
        MOD = 1000000007
        m = max(nums)

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        dp = [[0] * (m + 1) for _ in range(m + 1)]
        dp[0][0] = 1

        for num in nums:
            newDp = [[0] * (m + 1) for _ in range(m + 1)]

            for x in range(m + 1):
                for y in range(m + 1):
                    if dp[x][y] == 0:
                        continue

                    cur = dp[x][y]

                    newDp[x][y] = (newDp[x][y] + cur) % MOD

                    nx = gcd(x, num)
                    newDp[nx][y] = (newDp[nx][y] + cur) % MOD

                    ny = gcd(y, num)
                    newDp[x][ny] = (newDp[x][ny] + cur) % MOD

            dp = newDp

        ans = 0
        for g in range(1, m + 1):
            ans = (ans + dp[g][g]) % MOD

        return ans