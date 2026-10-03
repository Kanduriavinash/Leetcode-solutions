class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        self.getParenthesis(0, 0, "", n, res)
        return res

    def getParenthesis(self, open, close, s, n, res):
        if len(s) == 2 * n:
            res.append(s)

        if open < n:
            self.getParenthesis(open + 1, close, s + "(", n, res)

        if close < open:
            self.getParenthesis(open, close + 1, s + ")", n, res)