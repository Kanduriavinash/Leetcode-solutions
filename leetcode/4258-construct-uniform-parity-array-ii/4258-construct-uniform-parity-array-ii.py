class Solution(object):
    def uniformArray(self, nums1):
        return min(nums1) % 2 == 1 or all(x % 2 == 0 for x in nums1)