import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        while stones and len(stones) > 1:
            s1 = heapq.heappop_max(stones)
            s2 = heapq.heappop_max(stones)
            if s1 < s2:
                heapq.heappush_max(stones, s2 - s1)
            elif s1 > s2:
                heapq.heappush_max(stones, s1 - s2)
        
        if stones:
            return stones.pop()
        
        return 0