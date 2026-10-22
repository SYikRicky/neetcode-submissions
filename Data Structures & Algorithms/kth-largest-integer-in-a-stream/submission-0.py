import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k: int = k
        heapq.heapify(nums)
        self.nums: list[int] = nums
        
    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        while len(self.nums) > self.k:
            heapq.heappop(self.nums)
        return self.nums[0]