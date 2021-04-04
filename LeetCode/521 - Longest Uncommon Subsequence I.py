class Solution(object):
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        if len(a) > len(b):
            return len(a)
        elif len(a) < len(b):
            return len(b)
        elif a == b:
            return -1
        else:
            return len(a)
