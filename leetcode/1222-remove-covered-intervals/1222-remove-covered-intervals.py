class Solution(object):
    def removeCoveredIntervals(self, intervals):
        intervals.sort(key=lambda x: (x[0], -x[1]))

        count = 0
        end = 0

        for l, r in intervals:
            if r > end:
                count += 1
                end = r

        return count