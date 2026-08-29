class Solution(object):
    def lexicographicallySmallestArray(self, nums, limit):
        n = len(nums)

        arr = sorted((nums[i], i) for i in range(n))
        ans = nums[:]

        start = 0

        for end in range(1, n + 1):
            if end == n or arr[end][0] - arr[end - 1][0] > limit:
                values = [arr[i][0] for i in range(start, end)]
                indices = sorted(arr[i][1] for i in range(start, end))

                for i in range(len(values)):
                    ans[indices[i]] = values[i]

                start = end

        return ans