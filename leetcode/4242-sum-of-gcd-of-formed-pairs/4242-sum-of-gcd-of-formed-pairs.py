from fractions import gcd
class Solution(object):
    def gcdSum(self, nums):
        prefix = []
        mx = 0

        for x in nums:
            if x > mx:
                mx = x
            prefix.append(gcd(x, mx))

        prefix.sort()

        ans = 0
        i, j = 0, len(prefix) - 1
        while i < j:
            ans += gcd(prefix[i], prefix[j])
            i += 1
            j -= 1

        return ans