class Solution(object):
    def minSumOfLengths(self, arr, target):
        n = len(arr)
        INF = n + 1
        
        # best[i] = minimum length of a valid subarray
        # completely inside arr[0:i]
        best = [INF] * (n + 1)
        
        prefix = 0
        seen = {0: 0}
        ans = INF
        
        for i in range(1, n + 1):
            prefix += arr[i - 1]
            best[i] = best[i - 1]
            
            if prefix - target in seen:
                j = seen[prefix - target]
                length = i - j
                
                # Previous subarray must end before j
                if best[j] != INF:
                    ans = min(ans, length + best[j])
                
                best[i] = min(best[i], length)
            
            seen[prefix] = i
        
        return -1 if ans == INF else ans