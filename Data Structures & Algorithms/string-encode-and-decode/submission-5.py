class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = [ str(len(word)) + "|" + word for word in strs ]
        return "".join(encoded)
            

    def decode(self, s: str) -> List[str]:
        res = []
        while s:
            size = ""
            for char in s:
                if char == "|":
                    break
                size += char
            start = len(size)+1 # 10|10...
            end = start + int(size)
            temp = "".join(s[start : end])
            res.append(temp)
            s = s[end:]
        return res
