class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        res = []
        for num in nums:
            count[num] += 1

        for key, val in count.items():
            if len(res) < k:
                res.append(key)
            else:
                for num in res:
                    if val > count[num]:
                        print(f"Removing {num}")
                        res.remove(num)
                        print(f"Adding {key}")
                        res.append(key)
        return res