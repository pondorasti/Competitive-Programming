class Solution(object):
    def minSideJumps(self, obstacles):
        """
        :type obstacles: List[int]
        :rtype: int
        """
        dp = []
        for lane in range(3):
            sampleArr = []
            for _ in range(len(obstacles)):
                sampleArr.append(10000000)

            if lane == 1:
                sampleArr[0] = 0
            else:
                sampleArr[0] = 1

            dp.append(sampleArr)

        for index in range(1, len(obstacles)):
            for lane in range(3):
                if obstacles[index] == lane + 1:
                    continue
                for prevLane in range(3):
                    if obstacles[index - 1] == prevLane + 1 or obstacles[index] == prevLane + 1:
                        continue

                    if prevLane == lane:
                        dp[lane][index] = min(
                            dp[lane][index], dp[prevLane][index - 1])

                    else:
                        dp[lane][index] = min(
                            dp[lane][index], dp[prevLane][index - 1] + 1)

        size = len(obstacles) - 1
        ans = min(dp[0][size], dp[1][size], dp[2][size])

        return ans
