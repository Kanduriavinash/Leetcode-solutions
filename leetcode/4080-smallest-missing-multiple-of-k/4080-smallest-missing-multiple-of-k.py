class Solution(object):
    def missingMultiple(self, nums, k):
        s = set(nums)

        multiple = k

        while multiple in s:
            multiple += k

        return multiple