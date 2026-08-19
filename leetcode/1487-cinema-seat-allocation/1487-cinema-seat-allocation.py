class Solution(object):
    def maxNumberOfFamilies(self, n, reservedSeats):
        reserved = {}

        # Store reserved seats row-wise
        for row, seat in reservedSeats:
            if row not in reserved:
                reserved[row] = set()
            reserved[row].add(seat)

        ans = (n - len(reserved)) * 2

        # Check only rows having reserved seats
        for seats in reserved.values():

            # Seats 2,3,4,5
            left = all(seat not in seats for seat in [2, 3, 4, 5])

            # Seats 4,5,6,7
            middle = all(seat not in seats for seat in [4, 5, 6, 7])

            # Seats 6,7,8,9
            right = all(seat not in seats for seat in [6, 7, 8, 9])

            if left and right:
                ans += 2
            elif left or middle or right:
                ans += 1

        return ans