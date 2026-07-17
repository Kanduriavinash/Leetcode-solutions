class Solution(object):
    def gcdValues(self, nums, queries):
        from bisect import bisect_right

        mx = max(nums)

        freq = [0] * (mx + 1)
        for x in nums:
            freq[x] += 1

        exact = [0] * (mx + 1)

        for g in range(mx, 0, -1):
            cnt = 0
            for multiple in range(g, mx + 1, g):
                cnt += freq[multiple]

            pairs = cnt * (cnt - 1) // 2

            multiple = g * 2
            while multiple <= mx:
                pairs -= exact[multiple]
                multiple += g

            exact[g] = pairs

        prefix = [0] * (mx + 1)
        for i in range(1, mx + 1):
            prefix[i] = prefix[i - 1] + exact[i]

        ans = []
        for q in queries:
            ans.append(bisect_right(prefix, q))

        return ans