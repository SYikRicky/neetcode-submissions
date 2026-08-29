class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for idx, val in enumerate(temperatures):
            if len(stack) == 0:
                stack.append(idx)
            while stack and temperatures[stack[-1]] < val:
                temp_idx = stack.pop()
                res[temp_idx] = idx - temp_idx
            stack.append(idx)
        return res
