class Solution(object):
    def maxActiveSectionsAfterTrade(self, s):
        """
        :type s: str
        :rtype: int
        """
        ones = s.count('1')

        # Augment with '1' at both ends
        t = '1' + s + '1'

        # Run-length encoding
        runs = []
        i = 0
        while i < len(t):
            j = i
            while j < len(t) and t[j] == t[i]:
                j += 1
            runs.append((t[i], j - i))
            i = j

        ans = ones

        # Check every interior block of 1's
        for i in range(1, len(runs) - 1):
            if (runs[i][0] == '1' and
                runs[i - 1][0] == '0' and
                runs[i + 1][0] == '0'):
                gain = runs[i - 1][1] + runs[i + 1][1]
                ans = max(ans, ones + gain)

        return ans