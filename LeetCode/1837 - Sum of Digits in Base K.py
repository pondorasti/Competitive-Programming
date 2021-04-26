from math import log, floor


class Solution(object):
    def sumBase(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        # converted_number = 0
        digits_sum = 0
        while n:
            power = floor(log(n, k))
            nr_fits = int(n / k ** power)
            # converted_number = converted_number * 10 + nr_fits
            digits_sum += nr_fits
            n -= k ** power * nr_fits

        return digits_sum
