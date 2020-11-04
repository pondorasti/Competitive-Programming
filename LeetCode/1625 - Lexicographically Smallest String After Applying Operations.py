class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        step = None
        if len(s) % 2 == 0 and b % 2 == 0:
            step = 2
        else:
            step = 1
        
        answer = None
        permutations = s + s
        for start in range(0, len(s), step):
            end = start + len(s)
            slice = permutations[start:end]
            
            for iteration in range(0, 10):
                potential_answer = ""
                for index in range(0, len(s)):
                    new_digit = None
                    if index % 2 == 0:
                        new_digit = slice[index]
                    else:
                        new_digit = (int(slice[index]) + iteration * a) % 10
                    potential_answer = potential_answer + str(new_digit)
                
                print(potential_answer)
                if answer == None or answer > potential_answer:
                    answer = potential_answer
            print()
        
        return answer
