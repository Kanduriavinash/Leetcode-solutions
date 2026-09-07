class Solution(object):
    def distinctSubseqII(self, s):
        MOD = 10**9 + 7

        # dp[c] = number of distinct subsequences
        # that were created by using character c last
        dp = [0] * 26

        total = 0

        for ch in s:
            c = ord(ch) - ord('a')

            # All existing subsequences + the character itself
            new = (total + 1) % MOD

            # Replace old subsequences ending in this character
            total = (total + new - dp[c]) % MOD

            dp[c] = new

        return total