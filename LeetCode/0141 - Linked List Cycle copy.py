# V1
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        
        last_number = None
        for number in nums:
            if number == last_number:
                return number
            last_number = number


# V2
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        visited = {-1}
        
        for number in nums:
            if number in visited:
                return number
            visited.add(number)
