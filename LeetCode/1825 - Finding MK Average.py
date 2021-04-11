class MKAverage(object):

    def __init__(self, m, k):
        """
        :type m: int
        :type k: int
        """
        self.arr = []
        self.m = m
        self.k = k

    def addElement(self, num):
        """
        :type num: int
        :rtype: None
        """
        self.arr.append(num)

    def calculateMKAverage(self):
        """
        :rtype: int
        """
        if len(self.arr) < self.m:
            return -1

        averageArr = self.arr[-self.m:]
        averageArr.sort()
        size = len(averageArr)
        averageArr = averageArr[(self.k):(size-self.k)]

        average = 0
        for number in averageArr:
            average += number

        average = average // len(averageArr)

        return average


# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()
