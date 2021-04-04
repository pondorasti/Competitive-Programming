class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """

        stack = []
        directories = path.split("/")
        for directory in directories:
            if directory == "" or directory == ".":
                continue
            elif directory == "..":
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(directory)

        ans = ""
        for directory in stack:
            ans += "/" + directory

        if ans == "":
            ans += "/"
        return ans
