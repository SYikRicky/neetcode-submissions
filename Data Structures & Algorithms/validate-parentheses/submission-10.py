class Solution:
    def isValid(self, s: str) -> bool:
        check = []
        for char in s:
            if char == "(" or char == "{" or char == "[":
                check.append(char)
            elif char == ")":
                if len(check) > 0:
                    if check.pop() != "(":
                        return False
                else:
                    return False
            elif char == "}":
                if len(check) > 0:
                    if check.pop() != "{":
                        return False
                else:
                    return False
            elif char == "]":
                if len(check) > 0:
                    if check.pop() != "[":
                        return False
                else:
                    return False

        return len(check) == 0