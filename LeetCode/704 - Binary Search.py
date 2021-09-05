# V1
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        
        while start <= end:
            mid = (start + end) // 2
            
            if nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                return mid
        
        return -1


# V2
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def recursive_search(start, end):
            mid = (start + end) // 2
            
            if start > end:
                return -1
            elif nums[mid] < target:
                return recursive_search(mid + 1, end)
            elif nums[mid] > target:
                return recursive_search(start, mid - 1)
            elif nums[mid] == target:
                return mid
            
        return recursive_search(0, len(nums) - 1)
