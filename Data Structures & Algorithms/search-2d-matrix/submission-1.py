class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        merge = []
        for sublist in matrix:
            merge += sublist 
        l, r = 0, len(merge) - 1
        while l <= r:
            m = l + (r - l) // 2
            if merge[m] == target:
                return True
            elif merge[m] < target:
                l = m + 1
            elif merge[m] > target:
                r = m - 1
        return False