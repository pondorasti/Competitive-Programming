class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        def sortTuple(val):
            return val[0]

        tuplesArr = []
        for index in range(len(nums)):
            tuplesArr.append((nums[index], index))

        # create ans array
        ans = []
        for _ in range(len(nums)):
            ans.append(0)

        # sort tuples by element
        tuplesArr.sort(key=sortTuple)

        prevValue = -1
        counter = 1
        for index in range(len(tuplesArr)):
            indexOfElement = tuplesArr[index][1]
            currentElement = tuplesArr[index][0]

            if prevValue == currentElement:
                ans[indexOfElement] = index - counter
                counter += 1
            else:
                ans[indexOfElement] = index
                prevValue = currentElement
                counter = 1

        return ans
