class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        
        count1 = 0          # total freq of "?" in first half
        left = 0            # total sum of left side

        # 1. first half
        for i in range(n//2):  
            if num[i] == '?':
                count1 += 1
            else:    
                left += int(num[i])

        count2 = 0         # total freq of "?" in second half
        right = 0	       # total sum of right side

        # 2. second half of the array			
        for i in range(n//2, n): 
            if num[i] == '?':
                count2 += 1
            else:    
                right += int(num[i])

        # 3. compute dif in sum and "?" count 
        diff = left - right       
        count_diff = count2 - count1

        # 4. Bob wins if "?" count is even AND each "?" in half count gets the max value
        half = count_diff // 2
        bob = (count_diff % 2 == 0) and (9 * half == diff)

        # 5. Alice wins if Bob can't win
        return not bob