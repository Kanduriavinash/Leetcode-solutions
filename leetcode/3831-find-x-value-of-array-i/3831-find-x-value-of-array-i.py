class Solution(object):
    def resultArray(self, nums, k):
        ans = [0] * k
        dp = [0] * k

        for num in nums:
            new_dp = [0] * k

            # Start a new subarray with just num
            r = num % k
            new_dp[r] += 1

            # Extend all previous subarrays
            for old_r in range(k):
                if dp[old_r] > 0:
                    new_r = (old_r * r) % k
                    new_dp[new_r] += dp[old_r]

            # Add counts to answer
            for r in range(k):
                ans[r] += new_dp[r]

            dp = new_dp

        return ans