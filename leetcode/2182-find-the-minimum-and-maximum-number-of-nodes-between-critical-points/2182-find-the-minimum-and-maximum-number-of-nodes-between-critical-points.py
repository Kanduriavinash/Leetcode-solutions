class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        critical = []
        pos = 1

        prev = head
        curr = head.next

        while curr and curr.next:
            if (curr.val > prev.val and curr.val > curr.next.val) or \
               (curr.val < prev.val and curr.val < curr.next.val):
                critical.append(pos)

            prev = curr
            curr = curr.next
            pos += 1

        if len(critical) < 2:
            return [-1, -1]

        min_dist = float('inf')

        for i in range(1, len(critical)):
            min_dist = min(min_dist, critical[i] - critical[i - 1])

        max_dist = critical[-1] - critical[0]

        return [min_dist, max_dist]