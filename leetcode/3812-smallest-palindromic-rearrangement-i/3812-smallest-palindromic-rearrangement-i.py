from collections import Counter

class Solution(object):
    def smallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        freq = Counter(s)

        left = []
        mid = ""

        for ch in sorted(freq.keys()):
            left.append(ch * (freq[ch] // 2))
            if freq[ch] % 2 == 1:
                mid = ch

        left = "".join(left)
        return left + mid + left[::-1]