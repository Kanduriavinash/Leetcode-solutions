class Solution(object):
    def countCommas(self, n):
        ans = 0
        power = 1000
        commas = 1

        while power <= n:
            count = min(n, power * 1000 - 1) - power + 1

            ans += count * commas

            power *= 1000
            commas += 1

        return ans