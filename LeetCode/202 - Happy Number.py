class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        def sumOfSquaredDigits(number):
            sum = 0

            while number:
                digit = number % 10
                sum += digit * digit
                number /= 10

            return sum

        appearances = set([n])
        while n != 1:
            n = sumOfSquaredDigits(n)
            if n in appearances:
                return False

            appearances.add(n)

        return True
