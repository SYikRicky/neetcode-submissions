class Solution:
    def mySqrt(self, x: int) -> int:
        res = 0
        l, r = 1, x
        while l <= r:
            m = l + (r - l) // 2
            sq = m * m
            if sq > x:
                r = m - 1
            elif sq <= x:
                res = max(res, m)
                l = m + 1
        return res