class Solution:
    def checkValidString(self, s: str) -> bool:
        return (f:=lambda s,b:min(accumulate(1-2*(c==b) for c in s)))(s,')')>=0<=f(s[::-1],'(')