class Solution(object):
    def countGoodRectangles(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        """

        maxLen = 0
        counter = 0
        for rectangle in rectangles:
            # You can find the maximal square within a rectangle
            maximalSquare = min(rectangle[0], rectangle[1])
            if maximalSquare > maxLen:
                maxLen = maximalSquare
                counter = 1
            elif maximalSquare == maxLen:
                counter += 1

        return counter
