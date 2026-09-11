class Solution(object):
    def totalNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: int
        """
        numbers = set()

        for a in range(len(digits)):
            if digits[a] == 0:
                continue

            for b in range(len(digits)):
                if b == a:
                    continue

                for c in range(len(digits)):
                    if c == a or c == b:
                        continue

                    if digits[c] % 2 == 0:
                        num = digits[a] * 100 + digits[b] * 10 + digits[c]
                        numbers.add(num)

        return len(numbers)