class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        seto = set(nums)
        for number in range(1, 2**31 - 1):
            if number not in seto:
                return number