from collections import Counter

class Solution(object):
    def maximumLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = Counter(nums)
        ans = 1

        if 1 in cnt:
            ans = max(ans, cnt[1] if cnt[1] % 2 else cnt[1] - 1)

        for x in cnt:
            if x == 1:
                continue

            length = 1
            cur = x

            while cnt[cur] >= 2:
                nxt = cur * cur
                if cnt.get(nxt, 0) == 0:
                    break
                length += 2
                cur = nxt

            ans = max(ans, length)

        return ans