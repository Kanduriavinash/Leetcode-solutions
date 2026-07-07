class Solution(object):
    def sumAndMultiply(self, n):
        """
        :type n: int
        :rtype: int
        """
        x = ""
        total = 0
        
        for ch in str(n):
            if ch != '0':
                x += ch
                total += int(ch)
        
        if x == "":
            return 0
        
        return int(x) * total