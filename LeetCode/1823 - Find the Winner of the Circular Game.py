class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """

        # make circle
        circle = []
        for index in range(n):
            circle.append(index + 1)

        currIndex = 0
        while len(circle) is not 1:
            nextInd = (currIndex + k - 1) % len(circle)
            del circle[nextInd]
            currIndex = nextInd % len(circle)

        return circle[0]
