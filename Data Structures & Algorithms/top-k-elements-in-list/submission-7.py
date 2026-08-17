class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        temp = defaultdict(list)
        res = []
        for num in nums:
            count[num] += 1

        for num, freq in count.items():
            temp[freq].append(num)

        for i in range(k):
            if temp.keys():
                max_freq = max(temp.keys())
            res += temp[max_freq]
            temp.pop(max_freq)

        return res
        