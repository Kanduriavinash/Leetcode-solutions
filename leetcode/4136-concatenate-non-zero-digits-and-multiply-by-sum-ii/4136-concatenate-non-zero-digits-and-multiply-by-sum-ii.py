class Solution(object):
    def sumAndMultiply(self, s, queries):
        MOD = 10**9 + 7
        n = len(s)

        prefSum = [0] * (n + 1)
        prefCnt = [0] * (n + 1)
        prefVal = [0] * (n + 1)

        for i, ch in enumerate(s):
            d = int(ch)

            prefSum[i + 1] = prefSum[i]
            prefCnt[i + 1] = prefCnt[i]
            prefVal[i + 1] = prefVal[i]

            if d != 0:
                prefSum[i + 1] += d
                prefCnt[i + 1] += 1
                prefVal[i + 1] = (prefVal[i] * 10 + d) % MOD

        pow10 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD

        ans = []

        for l, r in queries:
            digitSum = prefSum[r + 1] - prefSum[l]
            count = prefCnt[r + 1] - prefCnt[l]

            if count == 0:
                ans.append(0)
                continue

            x = (prefVal[r + 1] - prefVal[l] * pow10[count]) % MOD

            ans.append((x * digitSum) % MOD)

        return ans