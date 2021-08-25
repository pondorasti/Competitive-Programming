class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        squaredNumbers = []
        index = 0
        while True:
            squaredNumbers.append(index ** 2)
            index += 1
            if (index ** 2 > 2 ** 31):
                break

        for i in range(0, len(squaredNumbers)):
            if (squaredNumbers[i] > c):
                continue

            left = 0
            right = len(squaredNumbers) - 1

            while left <= right:
                mid = (left + right) // 2

                if (squaredNumbers[i] + squaredNumbers[mid] == c):
                    return True
                elif (squaredNumbers[i] + squaredNumbers[mid] < c):
                    left = mid + 1
                elif (squaredNumbers[i] + squaredNumbers[mid] > c):
                    right = mid - 1

        return False
