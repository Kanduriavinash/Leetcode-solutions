from collections import defaultdict
from typing import List

class Solution:
    def maxSubarrayLength(self, nums_: List[int], freqUpLim_: int) -> int:
        # 1. Initialize frequency map and window tracking variables
        numToFreq = defaultdict(int)
        startIdx = 0
        # Tracks count of distinct elements exceeding the frequency limit
        freqViolationsCnt = 0

        # 2. Expand the right boundary of the window
        for num in nums_:
            # 3. Update frequency and check for limit violations
            numToFreq[num] += 1
            if numToFreq[num] == freqUpLim_ + 1:
                freqViolationsCnt += 1

            # 4. Grow the maximum valid window size
            if freqViolationsCnt == 0:
                continue
            
            # 5. Slide window by moving left boundary to maintain max size
            numToFreq[nums_[startIdx]] -= 1
            if numToFreq[nums_[startIdx]] == freqUpLim_:
                freqViolationsCnt -= 1

            startIdx += 1

        # 6. Calculate the final maximum subarray length
        return len(nums_) - startIdx