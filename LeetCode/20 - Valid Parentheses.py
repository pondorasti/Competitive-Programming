class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for index in range(len(s)):
            stackLen = len(stack)
            if (stackLen > 0 and stack[stackLen - 1] == self.opposite(s[index])):
                stack.pop()
            else:
                stack.append(s[index])

        return len(stack) == 0

    def opposite(self, char):
        if char == ")":
            return "("
        elif char == "}":
            return "{"
        elif char == "]":
            return "["
