from math import comb

class Solution(object):
    def smallestPalindrome(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """

        # Frequency of characters
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        # Middle character (if any)
        mid = ""
        half = [0] * 26
        half_len = 0

        for i in range(26):
            if freq[i] % 2:
                mid = chr(i + ord('a'))
            half[i] = freq[i] // 2
            half_len += half[i]

        # Count distinct permutations of remaining half
        def count_perm(cnt):
            rem = sum(cnt)
            res = 1
            for x in cnt:
                if x:
                    res *= comb(rem, x)
                    if res >= k:
                        return k
                    rem -= x
            return res

        if count_perm(half) < k:
            return ""

        first = []

        for _ in range(half_len):
            for i in range(26):
                if half[i] == 0:
                    continue

                half[i] -= 1
                ways = count_perm(half)

                if ways >= k:
                    first.append(chr(i + ord('a')))
                    break
                else:
                    k -= ways
                    half[i] += 1

        left = "".join(first)
        return left + mid + left[::-1]