class Solution(object):
    def reverseDegree(self, s):
        ans = 0

        for i, c in enumerate(s, 1):
            rev = 26 - (ord(c) - ord('a'))
            ans += rev * i

        return ans