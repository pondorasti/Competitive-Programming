class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = 0
        dp = {}

        for val in range(target + 1):
            dp[val] = []

        for candidate in candidates:
            if candidate == target:
                dp[candidate].append([candidate])

            dp[candidate] = [[candidate]]

        for val in range(target + 1):
            if dp[val] == []:
                continue

            for candidate in candidates:
                if val + candidate > target:
                    continue

                for arr in dp[val]:
                    newArr = arr[:]
                    newArr.append(candidate)
                    dp[val + candidate].append(newArr)

        ans = []
        for arr in dp[target]:
            isUnique = True
            sortedArr = sorted(arr)
            for solution in ans:
                if solution == sortedArr:
                    isUnique = False
                    break

            if isUnique:
                ans.append(sortedArr)

        return ans
