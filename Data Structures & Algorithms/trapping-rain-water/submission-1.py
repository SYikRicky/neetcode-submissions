from collections import deque

class Solution:
    def trap(self, height: List[int]) -> int:
        max_l = []
        max_r = deque()
        l = 0
        for h in height:
            max_l.append(l)
            l = max(l, h)
        r = 0
        for h in height[::-1]:
            max_r.appendleft(r)
            r = max(r, h)
        res = []
        for i, h in enumerate(height):
            area = min(max_l[i], max_r[i]) - h
            if area > 0:
                res.append(area)
        return sum(res)