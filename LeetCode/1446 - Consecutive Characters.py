class Solution:
    def maxPower(self, s: str) -> int:
        best_answer = 1
        current_answer = 1
        last_char = None
        for char in s:
            if last_char == char:
                current_answer += 1
            else:
                if current_answer > best_answer:
                    best_answer = current_answer
                current_answer = 1
                last_char = char
        
        if current_answer > best_answer:
            best_answer = current_answer
                
        return best_answer
