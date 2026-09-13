class Solution(object):
    def largestOverlap(self, img1, img2):
        a = [(i, j) for i in range(len(img1)) 
             for j in range(len(img1)) if img1[i][j]]

        b = [(i, j) for i in range(len(img2)) 
             for j in range(len(img2)) if img2[i][j]]

        count = {}
        ans = 0

        for x1, y1 in a:
            for x2, y2 in b:
                shift = (x2 - x1, y2 - y1)
                count[shift] = count.get(shift, 0) + 1
                ans = max(ans, count[shift])

        return ans