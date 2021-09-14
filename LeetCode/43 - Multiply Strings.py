class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        digits_table = { "0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9 }
        
        
        def convert(num):
            ans = 0
            
            for digit in num:
                ans = ans * 10 + digits_table[digit]
                
            return ans
        
        
        return f"{convert(num1) * convert(num2)}"