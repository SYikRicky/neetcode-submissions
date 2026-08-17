class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        temp = {}
        res = []
        for num in nums:
            count[num] += 1

        for num, freq in count.items():
            temp[freq] = num

        for i in range(k):
            max_freq = max(temp.keys())
            res.append(temp[max_freq])
            temp.pop(max_freq)

        return res
        