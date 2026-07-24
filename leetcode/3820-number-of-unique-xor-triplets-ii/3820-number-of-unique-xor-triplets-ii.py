class Solution(object):
    def uniqueXorTriplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        vals = list(set(nums))

        s1 = set(vals)
        s2 = set()

        for a in vals:
            for b in vals:
                s2.add(a ^ b)

        ans = set()
        for x in s2:
            for v in vals:
                ans.add(x ^ v)

        return len(ans)