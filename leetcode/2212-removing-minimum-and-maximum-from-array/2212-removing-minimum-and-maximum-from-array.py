class Solution(object):
    def minimumDeletions(self, nums):
        n = len(nums)

        mn = nums.index(min(nums))
        mx = nums.index(max(nums))

        left = min(mn, mx)
        right = max(mn, mx)

        front = right + 1
        back = n - left
        both = (left + 1) + (n - right)

        return min(front, back, both)