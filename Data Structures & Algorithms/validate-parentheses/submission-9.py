class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        check = []
        for char in s:
            if char == "(" or char == "{" or char == "[":
                check.append(char)
            elif (
                char == ")" and check.pop() != "(" or
                char == "}" and check.pop() != "{" or
                char == "]" and check.pop() != "["
            ):
                return False
        return True
