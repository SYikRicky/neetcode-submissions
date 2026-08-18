class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = [ str(len(word)) + word for word in strs ]
        return "".join(encoded)
            

    def decode(self, s: str) -> List[str]:
        res = []
        while s:
            size = int(s[0])
            temp = "".join(s[1:size+1])
            res.append(temp)
            s = s[size+1:]
        return res
