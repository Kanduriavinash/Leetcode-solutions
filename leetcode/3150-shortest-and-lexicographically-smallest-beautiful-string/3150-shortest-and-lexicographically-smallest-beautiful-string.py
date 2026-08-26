class Solution(object):
    def shortestBeautifulSubstring(self, s, k):
        ans =""
        for i in range(len(s)):
            ones=0
            for j in range(i,len(s)):
                if s[j]=='1':
                    ones+=1
                if ones==k:
                    current=s[i:j + 1]

                    if(ans == "" or len(current)<len(ans) or (len(current) == len(ans) and current < ans)):
                        ans= current
                    break
        return ans 
       
