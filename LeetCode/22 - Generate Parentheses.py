class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        combinations = []

        def combination(ans, openP, closeP):
            if closeP == n:
                combinations.append(ans)
                return

            if openP > closeP:
                combination(ans + ")", openP, closeP + 1)

            if openP < n:
                combination(ans + "(", openP + 1, closeP)

        combination("", 0, 0)
        return combinations
